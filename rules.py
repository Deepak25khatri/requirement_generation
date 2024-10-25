# rules.py

FR_RULES = {
    "Token-based": [
        {
            "rule": "Consider the number of tokens",
            "description": "Number of tokens in a requirement candidate.",
            "intuition": "A requirement candidate that is too long or too short could indicate a non-requirement."
        },
        {
            "rule": "Check the number of alphabetic words",
            "description": "Number of alphabetic words in a requirement candidate.",
            "intuition": "Few alphabetic words in a requirement candidate could indicate a non-requirement."
        },
        {
            "rule": "Count one-character tokens",
            "description": "Number of one-character tokens in a requirement candidate.",
            "intuition": "Too many one-character tokens in a requirement candidate could indicate a non-requirement, e.g., section headings."
        },
        {
            "rule": "Check if it starts with an alphanumeric identifier",
            "description": "TRUE if a requirement candidate starts with an alphanumeric segment containing special characters such as periods and hyphens, otherwise FALSE.",
            "intuition": "Alphanumeric segments with special characters could indicate identifiers for requirements."
        },
        {
            "rule": "Avoid starting with trigger words",
            "description": "TRUE if a requirement candidate begins with a trigger word ('Note', 'Rationale', 'Comment'), otherwise FALSE.",
            "intuition": "A trigger word at the beginning of a requirement candidate is a strong indicator for a non-requirement."
        },
        {
            "rule": "Include measurement units when applicable",
            "description": "TRUE if a requirement candidate contains some measurement unit, otherwise FALSE.",
            "intuition": "The presence of measurement units increases the likelihood of a requirement candidate being a requirement."
        }
    ],
    "Syntactic": [
        {
            "rule": "Must contain a verb",
            "description": "TRUE if a requirement candidate has a verb per POS tags, otherwise FALSE.",
            "intuition": "A requirement candidate without a verb is unlikely to be a requirement."
        },
        {
            "rule": "Should preferably contain a modal verb",
            "description": "TRUE if a requirement candidate has a modal verb, otherwise FALSE.",
            "intuition": "The presence of a modal verb is a good indicator for a requirement candidate being a requirement."
        },
        {
            "rule": "Look for Noun Phrase followed by Verb Phrase with modal verb",
            "description": "TRUE if a requirement candidate contains a sequence composed of a Noun Phrase (NP) followed by a Verb Phase (VP) that includes a modal verb, otherwise FALSE.",
            "intuition": "Captures the presence of the NP preceding a modal VP. This NP typically acts as a subject for the VP."
        },
        {
            "rule": "May include conditional clauses",
            "description": "TRUE if a requirement candidate has a conditional clause, otherwise FALSE.",
            "intuition": "Conditional clauses are more likely to appear in requirements than non-requirements."
        },
        {
            "rule": "Can use passive voice",
            "description": "TRUE if a requirement candidate has passive voice through some dependency relation, otherwise FALSE.",
            "intuition": "Requirements not containing modal verbs may be specified in passive voice."
        },
        {
            "rule": "Can use 'to be' as root verb followed by adjective",
            "description": "TRUE if, in requirement candidate, there is some form of the verb 'to be' appearing as root verb followed by an adjective, otherwise FALSE.",
            "intuition": "This pattern is more likely to appear in requirements."
        },
        {
            "rule": "Can be written in present tense",
            "description": "TRUE if a requirement candidate has some root verb which is in present tense, otherwise FALSE.",
            "intuition": "Sometimes, requirements are written in present tense rather than with modal verbs."
        }
    ],
    "Semantic": [
        {
            "rule": "Include action verbs conveying motion or change of status",
            "description": "TRUE if a requirement candidate has some verb conveying motion or change of status, otherwise FALSE.",
            "intuition": "Action verbs are common in requirements for describing behaviors and state changes."
        },
        {
            "rule": "Can include stative verbs for describing system properties",
            "description": "TRUE if a requirement candidate has some stative verb, otherwise FALSE.",
            "intuition": "Stative verbs are common in requirements for describing system properties."
        }
    ],
    "Frequency-based": [
        {
            "rule": "Use consistent and frequent identifier patterns",
            "description": "Maximum frequency level (high, medium, low) associated with the identifier pattern with which a given requirement candidate starts.",
            "intuition": "A frequent id pattern in a requirement candidate is likely to signify a requirement. This is because alphanumeric are prevalently used for marking requirements."
        },
        {
            "rule": "Use the most frequent modal verb of the requirement set",
            "description": "TRUE if a requirement candidate contains the most frequent modal verb of the RS, otherwise FALSE.",
            "intuition": "While a consistent application of modal verbs cannot be guaranteed, the most frequent modal verb is a strong indicator for requirements."
        },
        {
            "rule": "Include highly frequent noun phrases that signify core concepts",
            "description": "TRUE if a requirement candidate contains a highly frequent (top 1%) NP in the RS, otherwise FALSE.",
            "intuition": "Highly frequent NPs (after stopword removal) often signify core concepts, e.g., the system and its main components. These concepts are more likely to appear in requirements."
        }
    ],
    "EARS": [
        {
            "rule": "Must be triggered by an event",
            "description": "TRUE if a requirement candidate contains an event and a corresponding system response, otherwise FALSE.",
            "intuition": "Functional requirements often describe system behaviors triggered by specific events."
        },
        {
            "rule": "Specify the system's behavior during a particular state",
            "description": "TRUE if a requirement candidate includes a description of system behavior under a specific state, otherwise FALSE.",
            "intuition": "Requirements should outline system behavior while in certain states."
        },
        {
            "rule": "Identify the system response to undesired events or conditions",
            "description": "TRUE if a requirement candidate includes an undesired event and a corresponding system response, otherwise FALSE.",
            "intuition": "Requirements may specify actions in response to unwanted behaviors."
        }
    ],
    "RUPPS": [
        {
            "rule": "Identify actors involved",
            "description": "TRUE if a requirement candidate clearly identifies an actor, otherwise FALSE.",
            "intuition": "Functional requirements often specify who (e.g., 'user', 'admin') is interacting with the system."
        },
        {
            "rule": "Describe the complete scenario of interaction",
            "description": "TRUE if a requirement candidate describes a sequence of actions or events leading to an outcome, otherwise FALSE.",
            "intuition": "Functional requirements should clearly define scenarios involving system interaction."
        }
    ]
}



NFR_RULES = {
    "Token-based": FR_RULES["Token-based"],
    "Syntactic": FR_RULES["Syntactic"],
    "Semantic": [
        {
            "rule": "Avoid verbs conveying reasoning or intention",
            "description": "TRUE if a requirement candidate has some verb conveying reasoning or intention, otherwise FALSE.",
            "intuition": "Reasoning and intention are a common characteristic for non-requirements."
        },
        FR_RULES["Semantic"][0],  # Include action verbs
        FR_RULES["Semantic"][1]   # Include stative verbs
    ],
    "EARS": [
        {
            "rule": "State general properties of the system",
            "description": "TRUE if a requirement candidate defines an attribute that is always expected, regardless of events or states, otherwise FALSE.",
            "intuition": "Non-functional requirements often describe ongoing properties such as performance, availability, or reliability."
        }
    ],
    "RUPPS": [
        {
            "rule": "State preconditions for a requirement",
            "description": "TRUE if a requirement candidate specifies preconditions, otherwise FALSE.",
            "intuition": "Non-functional requirements often include conditions that must be met."
        },
        {
            "rule": "Define constraints on the system",
            "description": "TRUE if a requirement candidate specifies a constraint, otherwise FALSE.",
            "intuition": "Non-functional requirements usually define constraints related to performance, usability, or security."
        }
    ],
    "Frequency-based": FR_RULES["Frequency-based"]
}