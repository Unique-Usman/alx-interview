#!/usr/bin/python3
"""Solve the lockbox problem"""


def canUnlockAll(boxes):
    """Solve the lockbox problem"""
    res = {"0": True}
    for box in boxes:
        if not box:
            break
        for key in box:
            if key in res:
                continue
            else:
                if key < len(boxes):
                    res[f"{key}"] = True
                    for tri in boxes[key]:
                        if tri in res:
                            continue
                        res[f"{key}"] = True
    if len(boxes) == len(res):
        return True
    return False
