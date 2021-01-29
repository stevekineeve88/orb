import json

from flask import Blueprint, jsonify, request
from modules.Word.managers.SequenceManager import SequenceManager

sequence_api = Blueprint('sequence_api', __name__)


@sequence_api.route("/api/v1/sequence/perms/<sequence>", methods=["POST"])
def get_permutations(sequence: str):
    sequence_manager = SequenceManager()
    try:
        post = json.loads(request.data.decode())
        permutations = sequence_manager.search_permutations(
            sequence,
            sequence_length=post["sequence_length"] if "sequence_length" in post else len(sequence),
            prefixes=post["prefixes"] if "prefixes" in post else [],
            suffixes=post["suffixes"] if "suffixes" in post else [],
            contains=post["contains"] if "contains" in post else [],
            regexes=post["regexes"] if "regexes" in post else [],
            excludes=post["excludes"] if "excludes" in post else []
        )
        limit = post["limit"] if "limit" in post else 100
        limit = limit if 100 >= limit > 0 else 100
        offset = post["offset"] if "offset" in post else 0
        offset = offset if offset >= 0 else 0
        return jsonify({
            "success": True,
            "result": {
                "data": permutations.get_result_set(offset, limit),
                "meta": {
                    "total_count": len(permutations.get_result())
                }
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })
