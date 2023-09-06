from pathlib import Path

__DIR = Path(__file__).parents[0] / "schemas"


XML_VALIDATION = {
    "http://www.openarchives.org/OAI/2.0/oai_dc/": (__DIR / "oai_dc.xsd").as_posix(),
    "http://www.lido-schema.org": (__DIR / "lido-v1.0.xsd").as_posix(),
    "http://www.loc.gov/MARC21/slim": (__DIR / "MARC21slim.xsd").as_posix(),
    "http://www.loc.gov/mods/v3": (__DIR / "mods.xsd").as_posix(),
    "http://slubarchiv.slub-dresden.de/rights1": (__DIR / "rights1.xsd").as_posix(),
    "alto": (__DIR / "alto-v2.0.xsd").as_posix(),
    "metadata": None,
    "bag-info": None,
}
XML_VALIDATION_FAIL_ON_ERROR = False
