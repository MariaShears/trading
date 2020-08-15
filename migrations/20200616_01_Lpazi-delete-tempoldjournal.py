"""
delete TempOldJOurnal
"""

from yoyo import step

__depends__ = {'20200607_04_1YfWI-populate-journal-with-old-data-and-drop-old-table'}

steps = [
    step("DROP TABLE TempOldJOurnal;")
]
