from enum import StrEnum


class TMSHeaders(StrEnum):
    SUBJECT_CODE = "Subject Code"
    COURSE_NUMBER = "Course Number"
    INSTRUCTION_TYPE = "Instruction Type"
    INSTRUCTION_METHOD = "Instruction Method"
    SECTION = "Section"
    CRN = "CRN"
    COURSE_TITLE = "Course Title"
    DAYS_AND_TIME = "Days / Time"
    INSTRUCTOR = "Instructor"


class SectionHeaders(StrEnum):
    CRN = "CRN"
    SUBJECT_CODE = "Subject Code"
    COURSE_NUMBER = "Course Number"
    SECTION = "Section"
    CREDITS = "Credits"
    TITLE = "Title"
    CAMPUS = "Campus"
    INSTRUCTORS = "Instructors"
    INSTRUCTION_TYPE = "Instruction Type"
    INSTRUCTION_METHOD = "Instruction Method"
    MAX_ENROLL = "Max Enroll"
    ENROLL = "Enroll"
    SECTION_COMMENTS = "Section Comments"
    TEXTBOOKS = "Textbooks"


class AdditionalDetailsHeaders(StrEnum):
    COURSE_DESCRIPTION = "Course Description:"
    CREDITS = "Credits:"
    COLLEGE = "College:"
    DEPARTMENT = "Department:"
    RESTRICTIONS = "Restrictions:"
    SPECIAL_APPROVAL = "Special Approval:"
    CO_REQUISITES = "Co-Requisites:"
    PRE_REQUISITES = "Pre-Requisites:"
    CROSSLISTED = "Crosslisted/Also meets with:"
    REPEAT_STATUS = "Repeat Status:"


class ScheduleHeader(StrEnum):
    START_DATE = "Start Date"
    END_DATE = "End Date"
    TIMES = "Times"
    DAYS = "Days"
    BUILDING = "Building"
    ROOM = "Room"
