<!--
STYLE GUIDE FOR THE LAB GUIDES (this comment doesn't appear in the preview)
- Headings: one # title per document; ## for main sections; ### for sub-steps.
- Bullets: * for top-level bullets, - for sub-bullets.
- Label bullets: start with a bold label and a colon, e.g. **Ollama:** a free tool...
- Things to click or press: bold, with the exact wording on screen, e.g. click **+ New**, press **Return**.
- Commands: in a code block on their own line, never bold.
- Files, folders and email addresses: `code` style.
- Links: clickable with readable text, e.g. [ollama.com/download](https://ollama.com/download).
- Names: Webex (not WebEx), Claude desktop app, Ollama, uv, Lab 00 / Lab 01 / Lab 02 / Lab 03.
- Images: centered <p align="center"> block with a width, one <br> before and after.
- Placeholders: [PLACEHOLDER - description] on its own line, with an empty line before and after.
- Punctuation: full sentences end with a period; no double spaces; use an em dash (—), not --.
- Spacing: one <br> (with empty lines around it) before each section heading, except the first.
-->

# How to Save Your Work for Later

*Keep your apps, and everything Claude learned about them, so you can pick up where you left off.*

## What You Already Have

* **Your apps:** everything you built is in your lab folder, in your computer's home folder. Each lab has its own project folder (for example, `lab-01-knowledge-base`), with a start file and two guides.
* **Your AI models:** the models you downloaded with Ollama stay on your laptop.
* **What isn't saved automatically:** the conversation with Claude, including everything it knows about what you built and how you like to work. The steps below capture that in a file you keep.

<br>

## Step 1: Ask Claude for a Summary of Your Session

Before you leave, send this prompt in the same Cowork session you used for the labs:

> Write a detailed summary of everything we built in this session, so I can continue later in a new session. For each app, include what it does, its folder, how to start it (the start file), the AI models it uses, and anything I changed or improved along the way. Then add the main things I learned, any problems we solved, and ideas for what to build next. Save it as `My Workshop Summary.md` in my lab folder.

Check that `My Workshop Summary.md` appears in your lab folder. It's a Markdown file: you can read it in any text editor.

<br>

## Step 2: Save How You Like to Work as a Skill

A skill is a document that tells Claude how you like things done, so you don't have to explain it again in every session. If you saved a skill during the labs, this step brings it up to date. Send this prompt:

> Update `My Building Skill.md` in my lab folder with everything you learned in this session about how I like to work: my preferences for apps, guides, explanations and prompts, and the practices that worked well. Keep what's already in the file. If the file doesn't exist yet, create it.

<br>

## Step 3: If You Used a Lab PC, Take Your Folder With You

Lab PCs are cleared after each session, so copy your work before you leave:

* **Make a zip file:** right-click your lab folder and choose **Compress** (Mac) or **Send to → Compressed (zipped) folder** (Windows).
* **Copy the zip file** to a USB drive, or email or upload it to yourself.

On your own laptop, there's nothing to copy: your lab folder stays where it is.

<br>

## Pick Up Where You Left Off

* **Open the Claude desktop app** and start a new **Cowork** session with your lab folder, as in Lab 00. You can use your own Claude account: the workshop's demo accounts are only available for a limited time after the workshop.
* **Send this prompt:**

> Read `My Workshop Summary.md` (and `My Building Skill.md`, if it's there) in my lab folder. Then help me continue where I left off. Start by checking that my apps still run.

* **Start an app:** double-click its start file in its project folder, as in the labs.
