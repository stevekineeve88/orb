import json

from flask import Blueprint, jsonify, request

from modules.Word.managers.DictionaryManager import DictionaryManager

dictionary_api = Blueprint('dictionary_api', __name__)


@dictionary_api.route("/api/v1/dictionary/check/<word>", methods=["GET"])
def get_permutations(word: str):
    dictionary_manager = DictionaryManager()
    try:
        return jsonify({
            "success": True,
            "result": dictionary_manager.is_word(word)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })
