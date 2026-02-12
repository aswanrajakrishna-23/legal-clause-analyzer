import re

def analyze_clauses(text):
    clauses = []

    # Condition Clause
    for match in re.finditer(r'\b(?:if|in case)\b (.*?)(?:,| then | may | shall | will )(.*?)(?:\.|;|$)',
                             text, re.IGNORECASE):
        condition, consequence = match.groups()
        clauses.append({
            "type": "Condition Clause",
            "condition": condition.strip(),
            "consequence": consequence.strip()
        })

    # Exception Clause
    for match in re.finditer(r'\bunless\b (.*?)(?:,| may | shall | will )(.*?)(?:\.|;|$)',
                             text, re.IGNORECASE):
        condition, consequence = match.groups()
        clauses.append({
            "type": "Exception Clause",
            "condition": condition.strip(),
            "consequence": consequence.strip()
        })

    # Conditional Clause
    for match in re.finditer(r'\bprovided that\b (.*?)(?:,| may | shall | will )(.*?)(?:\.|;|$)',
                             text, re.IGNORECASE):
        condition, consequence = match.groups()
        clauses.append({
            "type": "Conditional Clause",
            "condition": condition.strip(),
            "consequence": consequence.strip()
        })

    return clauses
