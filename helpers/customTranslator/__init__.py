from googletrans import Translator as tr
import helpers.errors as ex




class ItalianToEnglishTranslator:
    
    def translate(self, value):
        translator = tr()
        if len(value)>500:
            raise ex.TextLengthExceededError(len(value))
        return translator.translate(value, dest="en", src="it").text
    
    
    def translateList(self, listOfValues):
        listOfTranslatedValues = []
        for value in listOfValues:
            try:
                listOfTranslatedValues.append(self.translate(value))
            except ex.TextLengthExceededError:
                longValueSplitted = self.__prepareValue(value)
                longValueTranslation = []
                for sentence in longValueSplitted:
                    longValueTranslation.append(self.translate(sentence))
                listOfTranslatedValues.append(longValueTranslation)
        return listOfTranslatedValues
    
    def __prepareValue(self, value, limit=-1):
        valueLength = len(value)
        if valueLength<limit:
            return [value]
        return value.split(".", maxsplit=limit)