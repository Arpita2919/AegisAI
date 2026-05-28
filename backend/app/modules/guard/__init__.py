"""LLM Guard package for prompt injection detection and mitigation."""

from importlib import import_module

__all__ = [
    "RegexFilter",
    "IntentClassifier",
    "DecisionEngine",
    "PromptSanitizer",
    "llm_guard",
]


def __getattr__(name):
    """Lazily load guard components so lightweight modules do not require torch."""
    if name == "RegexFilter":
        from .regex_rules import RegexFilter

        return RegexFilter
    if name == "IntentClassifier":
        from .intent_classifier import IntentClassifier

        return IntentClassifier
    if name == "DecisionEngine":
        from .decision_engine import DecisionEngine

        return DecisionEngine
    if name == "PromptSanitizer":
        from .sanitizer import PromptSanitizer

        return PromptSanitizer
    if name == "llm_guard":
        return import_module(".llm_guard", __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
