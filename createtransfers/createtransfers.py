#!/usr/bin/env python
# pylint: disable=invalid-name
"""This executable creates Archivematica sample and/or test transfers.

Possible reasons for creating transfers dynamically instead of just including
them in the repository include:

1. The transfers are very large.
2. The transfers contain directories or files whose names are in non-standard
   encodings which can bork on certain platforms.

Usage:

    python createtransfers.py -h

"""
import os
import shutil
import sys
from collections import namedtuple
from collections import OrderedDict

import createtransfersargs
import loggingconfig

TEST_TRANSFERS = "TestTransfers"
SAMPLE_PACKAGES = "sample-zip-packages"


class CreateTransferException(Exception):
    """Custom exception to aid with robust handling within this script."""

    pass


# Take the script up one level to execute so that we can place new files in
# different folders such as TestTransfers which exist at time of writing.
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a logger to provide feedback to the user.
LOGGER = loggingconfig.setup("INFO", "createtransfers")

# Configuration structure to retrieve filenames and encodings from.
VARIOUS_ENCODINGS = (
    {"dir_name": "windows_1252", "encoding": "cp1252", "file_name": "s\xf8ster"},
    {
        "dir_name": "shift_jis",
        "encoding": "shift-jis",
        "file_name": "\u307d\u3063\u3077\u308b\u30e1\u30a4\u30eb",
    },
    {"dir_name": "big5", "encoding": "big5", "file_name": "\u5ee3\u5dde"},
    {
        "dir_name": "emoji",
        "encoding": "utf-16",
        "file_name": (
            "hearts-{}.txt".format(
                "\u2764\uD83D\uDC96\uD83D\uDC99"
                "\uD83D\uDC9A\uD83D\uDC9B\uD83D"
                "\uDC9C\uD83D\uDC9D"
            ),
            "chess-{}.txt".format(
                "\u2655\u2656\u2657\u2658\u2659"
                "\u265A\u265B\u265C\u265D\u265E"
                "\u265F"
            ),
        ),
    },
    {"dir_name": "cp437", "encoding": "cp437", "file_name": ("caf\xe9", "a\xf1o")},
)


def encode_path(s, encoding="utf-16"):
    return s.encode(encoding, "surrogatepass").decode(encoding)


def create_file_and_write(file_name, file_path, encoding, dirs=False):
    """Given a filename and encoding write a file with self descriptive
    content to disk.
    """
    file_path = os.path.join(file_path, file_name)
    try:
        with open(file_path, "w") as fout:
            msg = "The name of this file is encoded with {} " "encoding.\n".format(
                encoding
            )
            if dirs:
                msg = (
                    "Part of the directory structure that this "
                    "file sits within has been encoded with {} encoding."
                    "\n".format(encoding)
                )
            fout.write(msg)
            LOGGER.info("Created: %s", file_path)
    except OSError as err:
        ret = f"Failed to open file: {file_path}, error: {err}"
        raise CreateTransferException(ret)


def rm_dirs_and_create(dir_path):
    """Remove pre-existing directory structures to write new ones out
    to disk.
    """
    rm_dirs(dir_path)
    try:
        os.makedirs(dir_path)
    except OSError as err:
        ret = f"Failed to make directory: {dir_path} {err}"
        raise CreateTransferException(ret)


def rm_dirs(dir_path):
    """Wrap shutils.rmtree in a useful manner."""
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
        except OSError as err:
            ret = f"Failed to remove dirtree: {dir_path} {err}"
            raise CreateTransferException(ret)


def create_transfer_collection(
    collection_path, media_path, media_n, new_media_dirname, media_ext
):
    """To create our transfers we are copying from elsewhere within the
    sample data repository to generate a new collection.
    """

    # Stat file, and return asap if it doesn't exist. If it does exist,
    # provide the user an idea about the size of the collection being
    # generated.
    try:
        stat_file(media_path, media_n)
    except CreateTransferException as err:
        LOGGER.error(err)
        return

    new_media_dir = os.path.join(collection_path, new_media_dirname)

    try:
        rm_dirs_and_create(new_media_dir)
    except CreateTransferException as err:
        LOGGER.error(err)
        return

    copy_media_location(media_path, new_media_dir, media_n, media_ext)


def copy_media_location(copy_media_path, new_media_dir, media_n, media_ext):
    """Create as maany copies of our sampledata files as required by the
    user in the argument media_n.
    """
    for i in range(media_n):
        new_media_fname = f"mediafile_{i}.{media_ext}"
        new_media_path = os.path.join(new_media_dir, new_media_fname)
        shutil.copyfile(copy_media_path, new_media_path)
    LOGGER.info("%s files created at %s", media_n, new_media_dir)


def stat_file(file_path, files_n):
    """Check that the file exists to make sure we're not referencing objects
    elsewhere in the transfer structure that don't exist. Return something
    useful if the files are available.
    """
    if not os.path.exists(file_path):
        ret = f"Cannot find media file at location {file_path}"
        raise CreateTransferException(ret)
    LOGGER.info(
        ("%s duplicated %s times " "will take up %sGB disk space"),
        file_path,
        files_n,
        ((os.path.getsize(file_path) * files_n) / 1024.0) / 1024.0 / 1024.0,
    )


def create_variously_encoded_files(zip_path=None):
    """Create files with strange (non-UTF8) encodings under
    TestTransfers/files_with_various_encodings/
    """
    sub_dir = "files_with_various_encodings"
    target_path = os.path.join(HERE, TEST_TRANSFERS, sub_dir)
    if zip_path:
        target_path = zip_path
    LOGGER.info("Transfer target path: %s", target_path)
    for encoding_info in VARIOUS_ENCODINGS:
        encoding_dir_path = os.path.join(target_path, encoding_info["dir_name"])
        try:
            rm_dirs_and_create(encoding_dir_path)
        except CreateTransferException as err:
            LOGGER.error(err)
            return
        encoding = encoding_info["encoding"]
        file_names = encoding_info["file_name"]
        if not isinstance(file_names, (tuple, list)):
            file_names = (file_names,)
        for fname in file_names:
            fname = encode_path(fname, encoding_info["encoding"])
            try:
                create_file_and_write(fname, encoding_dir_path, encoding)
            except CreateTransferException as err:
                LOGGER.error(err)
                return


def create_variously_encoded_dir_names(zip_path=None):
    """Create folders with strange (non-UTF8) encodings under
    TestTransfers/dirs_with_various_encodings/
    """
    sub_dir = "dirs_with_various_encodings"
    target_path = os.path.join(HERE, TEST_TRANSFERS, sub_dir)
    if zip_path:
        target_path = zip_path
    LOGGER.info("Transfer target path: %s", target_path)
    for encoding_info in VARIOUS_ENCODINGS:
        # Use the filename from the VARIOUS_ENCODINGS tuples minus the file
        # extension to give us something that looks like a directory name.
        dir_names = encoding_info["file_name"]
        if not isinstance(dir_names, (tuple, list)):
            dir_names = (dir_names,)
        for dir_ in dir_names:
            dir_ = encode_path(dir_)
            encoding_dir_path = os.path.join(
                target_path,
                encoding_info["dir_name"],
                os.path.splitext(os.path.basename(dir_))[0],
            )
            try:
                rm_dirs_and_create(encoding_dir_path)
            except CreateTransferException as err:
                LOGGER.error(err)
                return
            encoding = encoding_info["encoding"]
            try:
                create_file_and_write(
                    f"{encoding}_encoded_dirs.txt",
                    encoding_dir_path,
                    encoding,
                    dirs=True,
                )
            except CreateTransferException as err:
                LOGGER.error(err)
                return


def create_zip_packages_with_var_encoded_dirs():
    """Create zipped packages based on the auto-generated variously-encoded
    directory names.
    """

    # Control the name of these top-level folders so that we know that we can
    # recurse into them to zip the various contents.
    var_encoded_dirs = "variously-encoded-dirs"

    # Create zips with different directory name encodings in each.
    zip_path_dirs = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, var_encoded_dirs
    )
    create_variously_encoded_dir_names(zip_path_dirs)
    create_zip_dance(zip_path_dirs)


def create_zip_packages_with_var_encoded_fnames():
    """Create zipped packages based on the auto-generated variously-encoded
    filenames.
    """

    # Control the name of these top-level folders so that we know that we can
    # recurse into them to zip the various contents.
    var_encoded_files = "variously-encoded-files"

    # Create zips with different file name encodings in each.
    zip_path_files = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, var_encoded_files
    )
    create_variously_encoded_files(zip_path_files)
    create_zip_dance(zip_path_files)


def create_deep_zip_packages():
    """Create zipped packages based on the auto-generated deep-transfer set."""

    # Control the name of these top-level folders so that we know that we can
    # recurse into them to zip the various contents.
    deep_transfer = "deep-transfer"
    deep_zip_transfer = os.path.join(deep_transfer, "deep_zip_transfer")

    zip_path_deep = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, deep_zip_transfer
    )

    create_deep_transfers(
        zip_path=zip_path_deep,
        recursion_depth=createtransfersargs.DEFAULT_DEPTH,
        number_of_directories=createtransfersargs.DEFAULT_NUMBER_DIRS,
        number_of_files=createtransfersargs.DEFAULT_NUMBER_FILES,
    )
    # The first directory above is deliberately made one additional directory
    # down so that it can be zipped as one. First we have to come back up a
    # level which we do here.
    one_deep_zip_path = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, deep_transfer
    )
    create_zip_dance(one_deep_zip_path)


def create_large_zip_packages():
    """Create zipped packages based on the auto-generated performance testing
    suite.
    """

    # Create a single zip with one deep directory structure inside using the
    # application defaults.
    large_transfer = "large-transfer"
    large_zip_transfer = os.path.join(large_transfer, "large_zip_transfer")

    # Create a path where we will create a large zipped transfer folder.
    zip_path_large = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, large_zip_transfer
    )
    # Override the defaults to create a modest 1.1GB zip.
    create_large_test_transfers(performance_path=zip_path_large, image_n=35, video_n=35)
    # Like the deep transfer, we deliberately drop the large transfers down a
    # folder level. We come back a level here to zip it all at once.
    one_large_zip_path = os.path.join(
        HERE, TEST_TRANSFERS, SAMPLE_PACKAGES, large_transfer
    )
    create_zip_dance(one_large_zip_path)


def create_zip_dance(base_directory):
    """Perform various manoeuvers to create zip files from our content and move
    them into a suitable directory structure.
    """
    subdirs = [f for f in os.listdir(base_directory) if os.path.isdir(base_directory)]
    for dir_ in subdirs:
        # Create a temporary folder to provide structure inside our zip.
        sample_package = os.path.join(base_directory, "sample-package")
        rm_dirs_and_create(sample_package)
        dir_ = os.path.join(base_directory, dir_)
        # Move the folder we want to zip underneath the temporary folder.
        shutil.move(dir_, sample_package)
        # Re-create the previous folder as we will want to put the final zip
        # file into here.
        rm_dirs_and_create(dir_)
        # Make an archive from our directory.
        shutil.make_archive(dir_, "zip", sample_package)
        # Move the zip file from our temporary folder.
        move_from = f"{dir_}.zip"
        shutil.move(move_from, dir_)
        # Finally remove the temporary folder.
        rm_dirs(sample_package)


def create_large_test_transfers(performance_path=None, image_n=113, video_n=669):
    """Create large test transfers by copying existing sampledata files
    multiple times to specific subdirectories of
    TestTransfers/acceptance-tests/performance/
    """
    # Create a location for our large transfer.
    if not performance_path:
        performance_path = os.path.join(
            HERE, TEST_TRANSFERS, "acceptance-tests", "performance"
        )
    try:
        rm_dirs_and_create(performance_path)
    except CreateTransferException as err:
        LOGGER.error(err)
        return

    # Create dir images-17M-each-2G-total/ containing 2G of 17M image files.
    image_path = os.path.join(
        HERE,
        TEST_TRANSFERS,
        "manualNormalization",
        "manualNormalization",
        "preservation",
        "image_8.tif",
    )

    create_transfer_collection(
        performance_path, image_path, image_n, "images-17M-each", "tif"
    )

    # Create dir video-14M-each-10G-total/ containing 10G of 14M video files.
    video_path = os.path.join(HERE, "SampleTransfers", "Multimedia", "MakeUp.mov")

    create_transfer_collection(
        performance_path, video_path, video_n, "video-14M-each", "mov"
    )


def create_default_file(target_path):
    """Create a default object. Primarily for use with the deep-transfers
    functionality of this tool, but could equally be used elsewhere.
    """
    rm_dirs_and_create(target_path)

    default_file_path = os.path.join(target_path, "README.md")

    default_string = (
        "# Archivematica Deep Transfer Sample Set\n\n"
        "An arbitrarily generated depth of folders and files\n"
        "to test the recursive limits of Archivematica and its\n"
        "capability to generate metadata.\n"
    )

    LOGGER.info(
        "Creating default file to copy into deep " "transfer locations, %s",
        default_file_path,
    )

    with open(default_file_path, "w") as fout:
        fout.write(default_string)

    return default_file_path


def create_dir_and_fname_string(folder_no, ext=None):
    """Create unique folders names as we output our structure. We can create
    a hexadecimal string as a folder identifier. If we seek to use five digits
    then this will provide approx. 1,048,575 values to work with. Zero-fill is
    used to help  make our folder names look nice while doing this.
    """
    zero_fill = 5
    if ext is None:
        return f"{hex(folder_no + 1)}".replace("0x", "").zfill(zero_fill)

    return f"{hex(folder_no + 1)}.{ext}".replace("0x", "").zfill(
        zero_fill + len(ext) + 1
    )


FolderStructure = namedtuple("Structure", "depth dirs files")


def calculate_total_size(structure):
    """'depth' will be the min no. folders output.
    'dirs' becomes the no. folders per depth.
    Total dirs = dirs * depth
    'files' becomes the number of files per folder.
    Total files = files * total dirs
    """
    total_dirs = 0
    for dir_no in range(structure.depth):
        total_dirs = total_dirs + structure.dirs ** (dir_no + 1)

    total_files = structure.files * total_dirs

    LOGGER.info(
        "Received %s depth, %s dirs, and %s files. "
        "Outputting %s folders, and %s files.",
        structure.depth,
        structure.dirs,
        structure.files,
        total_dirs,
        total_files,
    )

    # We return this structure as an output of the unit testing developed
    # to understand the structure that we should output here.
    return FolderStructure(depth=structure.depth, dirs=total_dirs, files=total_files)


def create_folder_paths(folder_list, structure):
    """Create a listing of folder paths that will later be written out to
    disk.
    """
    new_folder_list = []
    for folder in folder_list:
        for folder_no in range(structure.dirs):
            new_folder_name = create_dir_and_fname_string(folder_no)
            numbered_path = os.path.join(folder, new_folder_name)
            new_folder_list.append(numbered_path)
    return new_folder_list


def create_structure(target, structure, default_file):
    """Create the structure of our deep transfer. First create and persist
    a list of file paths, and then use that list to output a set of test
    files to the 'n' required.
    """
    folder_dict = {}
    folder_list = []

    for folder_no in range(structure.dirs):
        new_folder_name = create_dir_and_fname_string(folder_no)
        folder_list.append(os.path.join(target, new_folder_name))

    folder_dict["l0"] = folder_list

    # Create structure for depth-1 as we've already created our first level
    # of folders at this point to feed into create folders.
    for folder_no in range(structure.depth - 1):
        # We create a new list with each node expanded to 'n' dirs.
        folder_list = create_folder_paths(folder_list, structure)
        # Create a placeholder in our dict for the structure we created.
        # folder_no+1 as we already have a [0] level described.
        folder_dict[f"l{folder_no + 1}"] = folder_list

    # Order the dictionary to make sure that we output the folders
    # as we created them.
    ordered_folders = OrderedDict(sorted(folder_dict.items()))

    # Output all of our folders, and under each create the desired number of
    # file names.
    for folder_list in ordered_folders.values():
        for path in folder_list:
            # Create path here, don't overwrite it by making it later,
            try:
                rm_dirs_and_create(path)
            except CreateTransferException as err:
                LOGGER.error(err)
                return

            for i in range(structure.files):
                new_path = os.path.join(path, create_dir_and_fname_string(i, "md"))
                shutil.copyfile(default_file, new_path)


def create_deep_transfers(**kwargs):
    """Entry point for our function to create deep transfers."""
    folder_structure = FolderStructure(
        depth=kwargs["recursion_depth"],
        dirs=kwargs["number_of_directories"],
        files=kwargs["number_of_files"],
    )
    # create a default folder from which to work from clear of the rest of
    # our environment.
    sub_dir = "deep_transfer"
    target_path = os.path.join(HERE, TEST_TRANSFERS, sub_dir)
    if kwargs.get("zip_path"):
        target_path = kwargs.get("zip_path")
    # We need some data to populate this location with. Create a small README
    # here and return the file path from which to copy from. Copying should
    # also be quicker than opening and closing 'n' files.
    default_file_path = create_default_file(target_path)
    calculate_total_size(folder_structure)
    return create_structure(target_path, folder_structure, default_file_path)


def main():
    """Entrypoint for createtransfers.py"""
    cmd_deep = "create-deep-transfers"
    cmd_large = "create-large-test-transfers"
    cmd_encodings = "create-variously-encoded-files"
    cmd_dirs = "create-variously-encoded-dir-names"
    cmd_large_zips = "create-large-zip-packages"
    cmd_deep_zips = "create-deep-zip-packages"
    cmd_fname_zips = "create-zip-packages-with-var-encoded-fnames"
    cmd_dir_zips = "create-zip-packages-with-var-encoded-dirs"

    # Create a named tuple to help us control what is passed
    # to each of the various commands.
    Command = namedtuple("Command", "cmd_name use_kwargs")

    commands = {
        cmd_deep: Command(cmd_name=create_deep_transfers, use_kwargs=True),
        cmd_large: Command(cmd_name=create_large_test_transfers, use_kwargs=False),
        cmd_encodings: Command(
            cmd_name=create_variously_encoded_files, use_kwargs=False
        ),
        cmd_dirs: Command(
            cmd_name=create_variously_encoded_dir_names, use_kwargs=False
        ),
        cmd_large_zips: Command(cmd_name=create_large_zip_packages, use_kwargs=False),
        cmd_deep_zips: Command(cmd_name=create_deep_zip_packages, use_kwargs=False),
        cmd_fname_zips: Command(
            cmd_name=create_zip_packages_with_var_encoded_fnames, use_kwargs=False
        ),
        cmd_dir_zips: Command(
            cmd_name=create_zip_packages_with_var_encoded_dirs, use_kwargs=False
        ),
    }

    argparser = createtransfersargs.get_parser(
        CMD_DEEP=cmd_deep,
        CMD_LARGE=cmd_large,
        CMD_ENCODINGS=cmd_encodings,
        CMD_DIRS=cmd_dirs,
        CMD_LARGE_ZIPS=cmd_large_zips,
        CMD_DEEP_ZIPS=cmd_deep_zips,
        CMD_FNAME_ZIPS=cmd_fname_zips,
        CMD_DIR_ZIPS=cmd_dir_zips,
    )

    if len(sys.argv) < 2:
        argparser.print_help()
        sys.exit(0)

    args = argparser.parse_args()
    if commands[args.subcommand].use_kwargs:
        return commands[args.subcommand].cmd_name(**vars(args))
    return commands[args.subcommand].cmd_name()


if __name__ == "__main__":
    main()
