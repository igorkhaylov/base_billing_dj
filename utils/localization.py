import json
import os
from typing import TypeVar


class Localization:
    """
        @param: default_language: The language to use if the message is not found in the current language
        @param: locales_path: Absolute path to the locales folder
        @param | : load_all: If True, all languages will be loaded at startup
    """
    _default_language = "en"
    _languages = []
    _loaded_languages = set()
    _locales_path = ""
    _messages = {}

    def __init__(self, default_language: str, locales_path: str, load_all: bool = True) -> None:
        self._default_language = default_language
        self._locales_path = locales_path
        self._languages = self._get_languages()
        if load_all:
            self._load_all_messages()
        else:
            self._messages[self._default_language] = self._load_messages(
                self._default_language)

    def _get_languages(self) -> list:
        languages = []
        for file in os.listdir(self._locales_path):
            if file.endswith(".json"):
                languages.append(file.split(".")[0])
        return languages

    def _load_messages(self, language) -> dict:
        messages = {}
        with open(self._locales_path + language + ".json", "r", encoding='utf-8') as f:
            messages = json.load(f)
        self._loaded_languages.add(language)
        return messages

    def _load_all_messages(self) -> None:
        for language in self._languages:
            self._messages[language] = self._load_messages(language)

    @property
    def languages(self) -> list:
        return self._languages

    def _get_message_keys_recursive(self, messages):
        keys = []
        for key in messages:
            if isinstance(messages[key], dict):
                keys += self._get_message_keys_recursive(messages[key])
            else:
                keys.append(key)
        return keys

    def check_messages_inconsistency(self, load_all: bool = True) -> None:
        default_lang_keys = set(self._get_message_keys_recursive(
            self._messages[self._default_language]))
        if load_all:
            self._load_all_messages()
        for language in self._loaded_languages:
            if language != self._default_language:
                lang_keys = set(self._get_message_keys_recursive(
                    self._messages[language]))
                if not default_lang_keys.issubset(lang_keys):
                    print("Inconsistency in language: " + language)
                    print("Missing keys: " +
                          str(default_lang_keys.difference(lang_keys)))
                    print("Extra keys: " +
                          str(lang_keys.difference(default_lang_keys)))
                elif lang_keys.difference(default_lang_keys):
                    print("Inconsistency in language: " + language)
                    print("Extra keys: " +
                          str(lang_keys.difference(default_lang_keys)))

    def translate(self, language: str, message_key_chain: str, params: dict = None) -> str:
        if language not in self._loaded_languages:
            self._messages[language] = self._load_messages(language)
        message_keys = message_key_chain.split(".")
        try:
            message = self._messages[language][message_keys[0]]
        except KeyError:
            return message_key_chain
        for key in message_keys[1:]:
            try:
                message = message[key]
            except KeyError:
                if language == self._default_language:
                    return message_key_chain
                else:
                    return self.translate(self._default_language, message_key_chain)
        try:
            if params is None:
                return message
            else:
                return message.format(**params)
        except KeyError:
            return message

    def key_messages(self, *args, **kwargs) -> dict:
        return {lang: self.translate(lang, *args, **kwargs) for lang in self.languages}

    # Alias Method Names
    t = translate
    km = key_messages


TLocalization = TypeVar('TLocalization', bound=Localization)
