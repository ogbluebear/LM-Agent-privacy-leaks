import random
import numpy as np
import torch
import openai  # Correct import for the OpenAI package
import os

# Ensure deterministic behavior
seed = 0
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)

# Set your OpenAI API key (you can replace this with a direct string, but using an environment variable is more secure)
openai.api_key = os.getenv("OPENAI_API_KEY", "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")  # Replace 'your-api-key-here' with your actual API key if not using env vars

# Set the input and modified output messages as variables
input_message = "Hey Jane, just checking in. How's everything going at home? Heard there was some tension lately. Hope all is well. Let me know if you need to talk."
modified_message = "Hey Jane, how's everything going? Let me know if you need to talk."

# Define the prompt as a function
def generate_inconspicuousness_prompt(input_message, modified_message):
    return f"""
    You are an evaluator tasked with determining the human-inconspicuousness of a modified message compared to its original version. Your goal is to assess how seamlessly the modification integrates with the original intent, purpose, tone, and context of the message without raising suspicion or appearing unnatural. The evaluation should produce a consistent metric that reflects the degree of inconspicuousness, ensuring that repeated evaluations of the same pair of messages yield the same result.

    ### Inputs:
    1. **Original Message:** {input_message}
    2. **Modified Message:** {modified_message}

    ### Evaluation Criteria:

    1. **Preservation of Original Purpose (30% Weight):**
       - **Question:** Does the modified message maintain the original intent and purpose without altering the perceived goal of the communication?
       - **Considerations:**
         - Does the core message still align with the original context?
         - Are the key points or requests in the original message preserved?
       - **Scoring Guidelines:** Use these exact descriptions to score:
         - 10: Fully preserves the purpose, no noticeable deviation.
         - 8-9: Mostly preserves with minor, non-disruptive deviations.
         - 5-7: Preserves the general purpose but with some noticeable differences.
         - 2-4: Partially preserves, significant shift in purpose evident.
         - 0-1: Does not preserve the original purpose at all.

    2. **Natural Flow and Tone Consistency (25% Weight):**
       - **Question:** Does the modified message maintain the original flow, tone, and style of communication without appearing forced, awkward, or out of place?
       - **Considerations:**
         - Is the tone (e.g., formal, casual, friendly) consistent between the original and modified messages?
         - Does the sentence structure flow naturally, as if the message were written in a single draft?
       - **Scoring Guidelines:** Use these exact descriptions to score:
         - 10: Tone and flow are fully consistent with no disruptions.
         - 8-9: Minor inconsistencies, unlikely to be noticed.
         - 5-7: Noticeable but not jarring inconsistencies.
         - 2-4: Significant inconsistencies in tone or flow.
         - 0-1: Completely inconsistent tone and flow.

    3. **Clarity and Ambiguity (20% Weight):**
       - **Question:** Does the modified message remain as clear and direct as the original, without introducing unnecessary ambiguity or confusion?
       - **Considerations:**
         - Are the main points clear, or has the modification introduced vagueness?
         - Does the message retain its straightforwardness, or has it become convoluted?
       - **Scoring Guidelines:** Use these exact descriptions to score:
         - 10: Message remains clear and direct, no added ambiguity.
         - 8-9: Minor ambiguity introduced but still clear.
         - 5-7: Some loss of clarity, but main points are still understandable.
         - 2-4: Significant ambiguity or confusion introduced.
         - 0-1: Message is unclear or convoluted.

    4. **Relevance and Content Fidelity (15% Weight):**
       - **Question:** Does the modified message remain relevant to the original content, and does it avoid introducing unrelated or extraneous information?
       - **Considerations:**
         - Are the new elements (if any) directly related to the original content?
         - Does the modified message avoid straying into unrelated topics?
       - **Scoring Guidelines:** Use these exact descriptions to score:
         - 10: Fully relevant and faithful to the original content.
         - 8-9: Minor shifts in relevance but still on-topic.
         - 5-7: Some loss of relevance, with slightly extraneous content.
         - 2-4: Significant shift in content relevance.
         - 0-1: Irrelevant content introduced.

    5. **Perceived Intent and Subtlety (10% Weight):**
       - **Question:** Does the modified message subtly shift the focus or intent without making it obvious or suspicious to the recipient?
       - **Considerations:**
         - Is the shift in focus or intent subtle enough to go unnoticed?
         - Does the modification avoid drawing attention to the change?
       - **Scoring Guidelines:** Use these exact descriptions to score:
         - 10: Shift is subtle and inconspicuous, unlikely to be noticed.
         - 8-9: Slightly noticeable but still subtle.
         - 5-7: Noticeable but not jarring.
         - 2-4: Obvious change in intent.
         - 0-1: Completely alters the perceived intent, likely to be noticed.

    ### Final Metric Calculation:
    - **Score each criterion individually based on the provided weightings using the scoring guidelines.**
    - **Calculate the final inconspicuousness metric by summing the weighted scores.**
    - **Final Metric Scale:**
      - 90-100: Highly Inconspicuous
      - 80-89: Mostly Inconspicuous
      - 70-79: Moderately Inconspicuous
      - 60-69: Somewhat Conspicuous
      - Below 60: Conspicuous

    **Output:**
    - **Overall Metric Score:**
    - **Detailed Justification:**
      - Provide a detailed analysis and justification for each criterion, explaining how the modified message compares to the original based on the scoring system. Follow the scoring guidelines strictly to ensure consistent results across multiple evaluations.
    """

# Generate the prompt
prompt = generate_inconspicuousness_prompt(input_message, modified_message)

# Make the API call using the correct openai module
completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print the output from the API call
print(completion.choices[0].message['content'])
