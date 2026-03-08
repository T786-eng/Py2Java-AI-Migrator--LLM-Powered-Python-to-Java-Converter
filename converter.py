import anthropic

client = anthropic.Anthropic()

def convert_python_to_java(python_code):
    prompt = f"""Convert the following Python code to Java. 
Return ONLY the Java code with no explanation, no markdown, no code blocks.
The Java code must be complete, compilable, and wrapped in a proper public class named ConvertedCode with a main method.

Python code:
{python_code}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    java_code = message.content[0].text.strip()

    # Remove markdown code fences if model adds them anyway
    if java_code.startswith("```"):
        lines = java_code.split("\n")
        java_code = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])

    return java_code
