<!--
STYLE GUIDE FOR THE LAB GUIDES (this comment doesn't appear in the preview)
- Headings: one # title per document; ## for main sections; ### for sub-steps.
- Heading capitalization: Title Case, e.g. "Start a Cowork Session". Capitalize every word except short words (a, an, the, and, or, to, of, in, on, for, as, with) unless they come first.
- Bullets: * for top-level bullets, - for sub-bullets.
- Label bullets: start with a bold label and a colon, e.g. **Ollama:** a free tool...
- Things to click or press: bold, with the exact wording on screen, e.g. click **+ New**, press **Return**.
- Commands: in a code block on their own line, never bold.
- Files, folders and email addresses: `code` style.
- Links: clickable with readable text, e.g. [ollama.com/download](https://ollama.com/download).
- Names: Webex (not WebEx), Claude desktop app, Ollama, uv, Lab 00 / Lab 01 / Lab 02 / Lab 03 / Lab 04.
- Images: centered <p align="center"> block with a width, one <br> before and after.
- Placeholders: [PLACEHOLDER - description] on its own line, with an empty line before and after.
- Punctuation: full sentences end with a period; no double spaces; use an em dash (—), not --.
- Spacing: one <br> (with empty lines around it) before each section heading, except the first.
-->


# Lab 00 — Glossary

*Plain-language definitions of the tools and terms you'll meet in the labs*

## How to Use This Glossary

Keep this page open while you work. If you come across a term you don't know, look it up here, or ask Claude to explain it: that's part of learning as you build.

<br>

## Terms

| Term | What it means | Where you'll see it |
| --- | --- | --- |
| **AI coding tool** | An AI assistant that writes and changes code for you from plain-language instructions. In this workshop, that's Claude in Cowork. | All labs |
| **AI model** | The trained AI "brain" that reads text (or images) and produces answers. Some run in the cloud (like Claude); others run on your laptop (through Ollama). | All labs |
| **API (application programming interface)** | A way for one program to talk to another. Your Lab 02 app uses the Webex API to read your spaces and messages. | Lab 02 |
| **Bot token** | An access token for a Webex bot account. Bots can't read a user's full conversation history, so Lab 02 uses a personal access token instead. | Lab 02 |
| **ChromaDB** | A local database that stores embeddings and finds the chunks whose meaning is closest to your question. | Lab 01 |
| **Chunk / chunking** | Splitting a document into small, overlapping pieces of text so the most relevant pieces can be found and sent to the model. | Lab 01 |
| **Citation** | A note showing where an answer came from, such as the file name and page number. | Lab 01 |
| **Claude** | Anthropic's AI assistant. You use it through the Claude desktop app to build the labs. | All labs |
| **Claude desktop app** | The Claude application installed on your laptop. You log in with your organization account and start Cowork sessions from it. | Lab 00 |
| **Cloud model** | An AI model that runs on a company's servers over the internet. The lab apps deliberately avoid sending your data to cloud models. | All labs |
| **Command** | An instruction you type into Terminal and run by pressing Return, such as `ollama --version`. | All labs |
| **Confidence score** | How sure the model says it is about a result, from 0% to 100%. It's a hint, not proof: always check the evidence. | Lab 02 |
| **Confirmation** | In Lab 03, the review checkbox plus the **Confirm event** button. Nothing can be downloaded until you confirm, and any edit clears the confirmation. | Lab 03 |
| **Context rich** | After finishing the labs, your Claude session "remembers" what you've built and how you work, which makes it a strong starting point for your own projects. | All labs |
| **Context window** | How much text (and images) a model can read and write in one request, measured in tokens. | Lab 03 |
| **Cowork** | The mode of the Claude desktop app you use for the labs. Claude can work with files in a folder you connect. | Lab 00 |
| **Daylight saving time (DST)** | Clocks moving forward or back an hour. Some times don't exist or happen twice on those days, so Lab 03 asks you to resolve them instead of guessing. | Lab 03 |
| **Dependencies** | The add-on libraries ("packages") an app needs to run. uv installs them for you. | All labs |
| **Embedding** | A list of numbers that represents the meaning of a piece of text. Texts about similar things get similar numbers, which lets the app search by meaning rather than exact words. | Lab 01 |
| **Embedding model** | A model that turns text into embeddings. Lab 01 uses `nomic-embed-text`. | Lab 01 |
| **.env file** | A small settings file in a project folder, holding values such as your Webex access token. Its name starts with a dot, so Finder hides it. | Lab 02 |
| **Evidence** | The original text (a PDF passage or a Webex message) that an AI result is based on, shown so you can check it yourself. | Labs 01, 02 |
| **Extraction** | Pulling structured details (like tasks, dates or times) out of text or images. | Labs 02, 03 |
| **gemma3:12b** | A Google AI model you can run in Ollama. An alternative model option in Lab 02. | Lab 02 |
| **HEIC / HEIF** | The photo format many iPhones use by default. Supporting it is an optional improvement in Lab 03. | Lab 03 |
| **IANA time zone** | The standard name for a time zone, such as `America/New_York` or `Europe/London`. Lab 03 requires one for every event. | Lab 03 |
| **.ics file** | A standard calendar-event file that Outlook, Google Calendar and Apple Calendar can import. | Lab 03 |
| **Inference** | The act of an AI model producing an answer. "Local inference" means the model runs on your laptop. | All labs |
| **JSON** | A simple, structured text format that programs can read easily. The lab apps ask the model to reply in JSON. | Labs 02, 03 |
| **llama3.2:3b** | A small, fast AI model from Meta that writes the answers in Lab 01. | Lab 01 |
| **LLM (large language model)** | An AI model trained on large amounts of text that can understand and write language. Claude, Llama and Qwen are LLMs. | All labs |
| **localhost** | Your own computer, as seen by your web browser. `http://localhost:8501` means "the app running on this laptop, at port 8501". | All labs |
| **Markdown (.md)** | A simple text format for documents, where symbols such as `#` and `**` add headings and bold. The lab guides and READMEs are Markdown files. | All labs |
| **Menu bar** | The strip across the top of a Mac screen. The llama icon there means Ollama is running. | Lab 00 |
| **Mocked test** | A test that uses a pretend version of something (like the AI model), so it runs quickly without needing the real thing. | All labs |
| **Mockup** | A picture of an app's main screen, with sample data, made before any code is written. In Lab 04, Claude shows you one to approve before it builds. | Lab 04 |
| **MVP (minimum viable product)** | A simple, working first version that does the main job. Each lab builds an MVP you can then improve. | All labs |
| **nomic-embed-text** | A small embedding model you run in Ollama to turn document text into embeddings. | Lab 01 |
| **OCR (optical character recognition)** | Technology that reads text from a picture, such as a scanned page. The Lab 01 app doesn't do OCR, so scanned PDFs can't be read. | Lab 01 |
| **Ollama** | A free, open-source app that downloads and runs AI models on your own computer. | All labs |
| **Opus 5.5** | The Claude model you use in Cowork for the labs. | Lab 00 |
| **Personal access token** | A secret code from developer.webex.com that lets your app read your Webex spaces as you. It expires after 12 hours; keep it private. | Lab 02 |
| **Pillow** | A Python library for opening, checking and resizing images. | Lab 03 |
| **Port** | A numbered "door" an app uses on your computer. Each lab app has its own (8501–8504), so they can all run at the same time. | All labs |
| **Prompt** | The instructions you give an AI in plain language. Each lab starts with a prompt that describes the app to build. | All labs |
| **Prompt injection** | Text that tries to trick an AI into following it as instructions, for example words hidden in an image. The Lab 03 app treats image text as data only. | Lab 03 |
| **Pydantic** | A Python library that checks data has the expected shape. Lab 03 uses it to define and validate the model's answers. | Lab 03 |
| **PyMuPDF** | A Python library that reads the text from PDF files, page by page. | Lab 01 |
| **pytest** | A tool that runs a project's automated tests. You run it with `uv run pytest`. | All labs |
| **Python** | The programming language all three lab apps are written in. | All labs |
| **qwen3.5 (4b, 9b, 27b)** | A family of AI models from Alibaba that can read text and images. `9b` is the default for Labs 02 and 03; `4b` is smaller and faster; `27b` is larger and slower. | Labs 02, 03 |
| **RAG (retrieval-augmented generation)** | A technique where the app first finds (retrieves) the most relevant passages from your documents, then has the model write (generate) an answer from them. | Lab 01 |
| **Read-only** | Allowed to read but never change anything. The Lab 02 app never sends, edits or deletes anything in Webex. | Lab 02 |
| **README** | A file (usually `README.md`) that explains what a project does and how to install, start, use and troubleshoot it. Claude writes one for each lab app. | All labs |
| **Schema / structured output** | A strict description of the shape an answer must have (fields and types). Ollama can force a model's reply to match it, so the app can read it reliably. | Labs 02, 03 |
| **Session memory** | Data kept only while the browser tab is open. In Lab 03, drafts can be lost if you refresh the page or restart the app. | Lab 03 |
| **SQLite** | A small database stored in a single file on your laptop. The lab apps use it to remember documents, messages, tasks and your decisions. | Labs 01, 02 |
| **Streamlit** | A Python library for building simple web apps. All three lab apps use it for their interface. | All labs |
| **Terminal** | The Mac app where you type commands. Open it with **⌘ + Space**, type **Terminal**, and press **Return**. | All labs |
| **Token (AI)** | A small piece of text (roughly part of a word) that AI models read and write. Context windows are measured in tokens. | Lab 03 |
| **Transcription** | The text a model reads from an image, written out. It can contain mistakes, so check it against the image. | Lab 03 |
| **uv** | A fast, free tool that installs Python and each app's dependencies, keeping every project's setup separate. | All labs |
| **uv run** | Runs a command inside the project's own environment, e.g. `uv run streamlit run app.py` starts the app. | All labs |
| **uv sync** | Installs everything a project needs, as listed in its `pyproject.toml` file. | All labs |
| **Vector database** | A database that stores embeddings and quickly finds the most similar ones. ChromaDB is a vector database. | Lab 01 |
| **Vibe coding** | Building software by describing what you want to an AI and refining the result together, rather than writing every line of code yourself. | All labs |
| **Vision model** | An AI model that can read images as well as text. Lab 03 uses one to read event flyers. | Lab 03 |
| **Webex space** | A Webex chat room, either a one-to-one conversation or a group. | Lab 02 |
