from modeltranslation.translator import translator, TranslationOptions

from EMPLOYEE.models import Department, Position

class DepartmentTranslate(TranslationOptions):
    fields = ('name',)

class PositionTranslate(TranslationOptions):
    fields = ('name',)



translator.register(Department, DepartmentTranslate)
translator.register(Position,PositionTranslate)