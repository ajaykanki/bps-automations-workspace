# Email Monitoring Service

- Should process each incoming email.
- Extract the subject line
- Authorize the sender using windmill_client
- Get all runnables of the sender
- For each runnable, check if the subject line fuzzily matches the runnable's path/summary/description
- Threshold score is 90%
- If the score is above the threshold, trigger the runnable
  - Check if the runnable requires a a single base64 encoded attachment or a list of file paths as "input_files",
  - If the runnable requires a single base64 encoded attachment trigger the runnable directly with the attachment
  - If the runnable requires a list of file paths as "input_files", save the attachments in a unique directory, trigger the runnable with the list of file paths as "input_files".
  - If the flow does not require any input files, trigger the runnable directly
  - FUTURE:
    - Get the runnable's JSON Schema
    - Extract structured data from the email body using AI
    - Trigger the runnable with the structured data

# Creating flows in windmill

- Must have the following input fields:
- input_files: list of file paths (optional)
- is_email_triggered: boolean (optional)
- conversation_id: string (optional)
- kwargs: dict (key value properties specific to the flow)
