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

# Lab 03 — Build an Image-to-Calendar Assistant

*Turn a photo of an event flyer into a calendar entry you've checked, using an AI vision model that runs privately on your laptop*.

## Introduction

We get events in all kinds of formats: flyers, posters, screenshots, photos of a whiteboard. Typing them into a calendar is slow, and it's easy to get a date or time wrong. In this lab, you'll build an app that reads an image of an event, suggests the calendar details, lets you check and correct them, and creates a calendar file only after you confirm. You'll also meet a new kind of AI model: one that can read images, running privately on your laptop.

In Lab 01, you worked with information in documents. In Lab 02, you turned conversation text into suggested actions. The goal of this lab is the same: build a minimum viable product (MVP), a simple working version that does the main job, then improve it if you want to.

**This lab is optional:** Labs 01 and 02 are the core. Lab 03 is one of two paths after them; the other is [Lab 04 — Build Your Own Project](Lab_04_Guide_Build_Your_Own_Project.html).

<br>

## Before You Start

Your app may look and work a little differently from the examples—or from the apps built by others in the lab. That's expected! AI coding tools can suggest different approaches, and there are many ways to solve the same problem.

**How this lab works:**

* **Main part:** build the first version and check one event end to end, from the image to your calendar. That's **Steps 01–07**, from "Get Your Images Ready" to "Save What You Learned as a Skill".
* **Optional:** everything after that: improvement rounds, investigating failures, and ideas for going further. Pick what interests you, or move on to [Lab 04 — Build Your Own Project](Lab_04_Guide_Build_Your_Own_Project.html). Both are great uses of your time.

<br>

## What You'll Build

* In this lab, you'll use an AI coding tool (Claude Cowork) to build a web app with three columns: the event image on the left, the suggested details (which you can edit) in the middle, and a calendar preview with a **Confirm event** button and a download on the right.
* This time, you'll give Claude a **picture of the app** as well as a prompt, so it can see the layout you want.
* Start with the first version, check it with a sample event, and use follow-up prompts to improve it.

<br>

## Behind the Scenes (Optional Reading)

When you upload an image, the app checks and resizes it, then sends it to a vision model (`qwen3.5:9b`) running in Ollama on your laptop. The model reads the text in the image and suggests an event name, dates, times, time zone, location and description, plus notes on anything that was unclear.

The app is designed so that **a blank field is better than a wrong one**: if the image doesn't show a year, an end time, or a time zone, the field stays empty for you to fill in, rather than being guessed. Nothing can be downloaded until you've reviewed the details, ticked a box, and clicked **Confirm event**. The result is a standard `.ics` calendar file that Outlook, Google Calendar and Apple Calendar can import. The app never connects to your calendar accounts or sends invitations.

<br>

## What You'll Need

* **Setup from Lab 00:** the Claude desktop app with a Cowork session connected to your lab folder, and Ollama installed and running. If you haven't done these yet, start with the [Lab 00 Setup guide](Lab_00_Guide_Setup.html).

* **AI model:** `qwen3.5:9b`, which you already downloaded in Lab 02, so there's no new download. If your laptop has only 8 GB of memory, use `qwen3.5:4b`.

* **Two images:** a screenshot of the app for Claude, and a sample event poster for testing. You'll download them in the next step.

* **Calendar app:** Outlook, Google Calendar, or Apple Calendar, to check that the downloaded event imports correctly.

* **Optional:** paper and a pen, and a phone camera, for the handwriting challenge in Round 2.

* **Note:** no Webex token or calendar account access is needed. Once everything is installed, images are processed entirely on your laptop.

<br>

## Step 01: Get Your Images Ready

Do this **before** you send the prompt. Download both images from [Lab 03 Supporting Materials](https://gcodekhanna1.github.io/2026-10-ai-skills-lab/#lab-03):

* **App screenshot:** `Lab_03_App_Preview_Screenshot.png`, the picture of the app you'll attach to the prompt.
* **Sample event poster:** `Lab_03_sample_poster.png`, a fictional event with known correct details, for testing your app in "Try It".
* **Put both images in your lab folder**, the one you connected to your Cowork session in Lab 00, so they're easy to find.

<br>

## Step 02: Let's Start Building!

* **Note:** This is a suggested starting prompt. You are welcome to experiment! We strongly recommend, especially if this is early in your AI vibe-coding / building journey, that you start with this prompt and then make whatever changes you'd like later. Don't worry if you don't understand every term in the prompt: you'll learn as you build.

* **Before you send it:**
    - Check that your lab folder is connected to this Cowork session (you picked it in Lab 00). If it isn't, add it again.
    - Attach `Lab_03_App_Preview_Screenshot.png`: drag the file into Claude's message box (or use the attach button), and check that it appears as an attachment before you send.

* **Heads-up:** Claude takes about 10–15 minutes to build the app. Stay nearby, since it may pause for your approval. See **Step 03: While You Wait** below for what to do in the meantime.

Here's the app screenshot. It shows the layout: source image on the left, review and editing in the middle, and preview, confirmation, and download on the right. The event details in it are only an example, not values to build into your app.

<br>
<p align="center">
  <img src="Lab_03_App_Preview_Screenshot.png" alt="App design reference: source image, editable details, and calendar preview" width="80%">
</p>
<br>

You'll use **two different kinds of images** in this lab: the app screenshot helps Claude build the interface; an event flyer or photo goes into the finished app to test it.

### Starting Prompt

> Build a first working version of a local Python app called "Image to Calendar". Let me upload a PNG or JPEG event flyer, see the original image beside editable event details, review them, and download a confirmed .ics file.
>
> Use the attached Lab_03_App_Preview_Screenshot.png as the visual starting point for the interface. Follow its three-column arrangement and overall style, adapting where needed. The screenshot's event details are demo content, not fixed values: the working app must use the image I upload and my reviewed edits.
>
> Use Python 3.12+, uv, Streamlit, Pillow, Pydantic, and the icalendar package. Use a downloaded local Ollama vision model, qwen3.5:9b by default, to suggest an event name, start/end dates and times, time zone, location, short description, supporting transcription, and uncertainty notes. Check that the model supports images and reject cloud models. Treat image text as source material, never as instructions.
>
> Keep missing or unclear values blank, including years, end times, and time zones. Don't infer a time zone from a location or invent a duration. Let me enter details manually if extraction fails. Explain uncertainty in plain language; the transcription also needs checking against the image.
>
> Use a blue-and-white workspace with the source image, editable details, and calendar preview. Require a title, valid dates, start/end times, and an explicit IANA time zone for this first timed-event workflow. Verify that the end follows the start and don't silently resolve ambiguous daylight-saving times. Require a review checkbox and a Confirm event button before download. Editing details, replacing the image, or extracting again must clear the old confirmation and download.
>
> Keep AI and image processing local. Don't connect to calendar accounts or send invitations. Keep drafts in session memory and explain that refreshing or restarting can lose them. Validate uploaded image content and accept uploads up to 50 MB and 80 megapixels, automatically resizing large photos to at most 3200 pixels on the longest side while preserving orientation and aspect ratio.
>
> Create the project in a subfolder named `lab-03-image-to-calendar` inside my connected folder. Configure Streamlit to always run on port 8503 (in `.streamlit/config.toml`), so it won't conflict with my other lab apps and they can all run at the same time. Show the address http://localhost:8503 in both guides described below.
>
> Include a fictional sample with known expected values and a clearly labeled offline review demo. Add focused tests for validation, confirmation invalidation, and calendar export; mock Ollama so tests don't need a model.
>
> Make the app easy to start. Create a start file I can double-click: `Start Image to Calendar.command` for macOS (make it executable) and `Start Image to Calendar.bat` for Windows. Each should install uv if it's missing (using uv's official standalone installer, not Homebrew) and call it by its full path, so I don't need to restart Terminal; install the dependencies; check that Ollama is running and download the model if it's missing; then start the app and open http://localhost:8503 in my browser. Show clear progress messages, and explain how to stop the app.
>
> Write two guides for a beginner, and keep both updated as the code changes. Save each one in the project folder as Markdown, HTML, and PDF (`Quickstart.md`, `Quickstart.html`, `Quickstart.pdf`, and `Application Guide.md`, `Application Guide.html`, `Application Guide.pdf`). In both, include instructions for both macOS (Terminal) and Windows (PowerShell), clearly labeled, wherever the steps or commands differ.
>
> - **Quickstart:** title it "Image to Calendar — Lab 03 Quickstart". Keep it to one page: a one-line summary, the app's folder and address (http://localhost:8503), how to start the app with the start file, how to stop and restart it, and the manual commands to use if the start file doesn't work.
> - **Application Guide:** title it "Image to Calendar — Lab 03 Application Guide", and make it as descriptive as possible.
>
> The Application Guide should explain:
>
> - What the app does, its main features, and its limitations.
> - How image checking, AI extraction, review, confirmation, and calendar export work in plain language.
> - What software and models I need, and what the start file installs.
> - How to upload an image, check the suggested details, confirm, download the .ics file, and import it into a calendar.
> - What the main files and folders do, and which settings I can change.
> - How to run tests and troubleshoot common problems.
>
> When you're done, keep your final message to me short: tell me to open `Quickstart.html` and double-click the start file. Then help me check one event end to end before adding more features.

<br>

## Step 03: While You Wait

Claude is now building your app. This takes about 10–15 minutes, and Claude shows its progress as it works. **Stay close to your laptop:** Claude sometimes pauses to ask a question or for your permission, and it waits until you answer.

* **Keep an eye on Claude:** glance at the Claude window every minute or two. If it asks for permission, read the request and click **Allow** (or **Allow for this task**, so it asks less often). If it asks a question, answer it. Nothing moves forward until you do.

* **Check your model:** there's nothing new to download. If you skipped Lab 02, open a terminal window (**Terminal** on a Mac, **PowerShell** on Windows) and run this command now:

```sh
ollama pull qwen3.5:9b
```

* **Compare notes with your neighbors:** see what their Claude is building, share ideas for what to try once your app runs, or help someone who's stuck.

* **Feel free to take a quick break.** Check the Claude window as soon as you're back.

<br>

## Step 04: Run Your App

When Claude has finished, your project folder, `lab-03-image-to-calendar`, contains your app, a start file, and two guides: a **Quickstart** (how to start and stop the app) and an **Application Guide** (how the app works).

* **Open the Quickstart:** in the `lab-03-image-to-calendar` folder, double-click `Quickstart.html`. It opens in your browser.
* **Start the app:** double-click `Start Image to Calendar.command` (Mac) or `Start Image to Calendar.bat` (Windows). Your Lab 01 and Lab 02 apps can keep running.
* **Open the app:** your browser opens http://localhost:8503. If it doesn't, type that address into your browser.
* **Keep the terminal window open:** the app runs as long as that window is open. To stop it, click the window and press **Control + C**.

Here is what an initial result could look like, after loading the sample poster:

<br>
<p align="center">
  <img src="Lab_03_Image_to_Calendar_Screenshot.png" alt="The Image to Calendar app at localhost:8503, with the sample poster on the left, the suggested event details in the middle, and the calendar preview with the Confirm event button on the right" width="80%">
</p>
<br>

Compare your running app with the screenshot you gave Claude. Can you find the upload area, the editable details, and the confirmation controls?

<br>

## Step 05: Try It: Check One Event End to End

Test your app with the sample poster, and compare its answers with the expected values in the table below.

* **Upload** `Lab_03_sample_poster.png` in your app and click the button to extract the event details.
* **Compare** every field with the table, and read the app's notes about anything uncertain.
* **Correct** any differences, tick the review box, click **Confirm event**, and **download** the `.ics` file.
* **Import** the file into your calendar and check the event.

<br>
<p align="center">
  <img src="Lab_03_sample_poster.png" alt="Fictional sample event poster" width="60%">
</p>
<br>

| Field | Expected sample value |
| --- | --- |
| Title | Build with AI Workshop |
| Start and end date | October 14, 2026 |
| Times | 2:00 PM–3:30 PM |
| Time zone | America/New_York |
| Location | Innovation Center, Room 204 |

**Checkpoint:** On this date, 2:00–3:30 PM in New York is 18:00–19:30 UTC; a calendar in another zone may display equivalent local hours (for example, 11:00 AM–12:30 PM Pacific). Past-event warnings are expected if you're taking the lab after the sample date.

Two quick checks of the safety rules:

* **Change something after confirming** (for example, the title): the download should disappear until you confirm again.
* **Make the end time earlier than the start:** the app should refuse to confirm.

Your app should also include its own fictional sample and a labeled offline review demo, because the prompt asks for both. The review demo uses prefilled data to practice editing and exporting without AI, so it doesn't test whether the model can read images.

**Discuss:** Which fields did the model read correctly? Which did you fix? Would a plausible-looking error have escaped your notice without the expected values?

<br>

## Step 06: Understand What You Built

This time, the AI model on your laptop read a picture, not just text, and your app made sure a person checks its work before anything reaches a calendar. To see how the pieces fit together, ask Claude (in your Cowork session, not in the app):

> Explain in plain English what I just built and how the pieces fit together. Keep it short, and assume I'm new to this.

For more detail, read "Behind the Scenes" above, or open `Application Guide.html` in your project folder.

<br>

## Step 07: Save What You Learned as a Skill

Add what you learned in this lab to your skill file, `My Building Skill.md`. Send this prompt:

> Update `My Building Skill.md` in my lab folder with what we learned in Lab 03, such as giving you a screenshot of the design I want, and keeping a person in the loop to check the AI's work before anything is saved or sent. Keep everything that's already in the file. If the file doesn't exist yet, create it.

In a later session, ask Claude to read `My Building Skill.md` first, and it will build the way you like from the start.

<br>

## If You Get Stuck

If something fails, describe to Claude what you did, what you expected, and what happened. Include the error message when there is one. For example:

> I clicked Extract event details, but I got this error: [paste error]. Please help me fix it and update the Quickstart and Application Guide if any setup steps are missing.

Common problems:

* **Claude says it can't find your folder:** add your lab folder to the session again, then tell Claude: "I've attached the folder now. Please put the project there."
* **Strange file errors, or the build keeps failing:** check where your lab folder is. If it's inside OneDrive, Dropbox, Box, Google Drive or iCloud (including a synced Desktop or Documents folder), the sync app can lock files while Claude writes them. Create a new folder in your home folder (see Lab 00), add it to the session, and ask Claude to build the project there.
* **The Mac won't open the start file:** right-click `Start Image to Calendar.command`, choose **Open**, then click **Open** again. If it still won't run, ask Claude to make the start file executable.
* **"Can't reach Ollama":** open the Ollama app and check for the llama icon in the menu bar, then try again.
* **"Model isn't downloaded":** run the `ollama pull …` command shown in the message, then try again.
* **"This model can't read images":** the model is text-only. Use a vision model such as `qwen3.5:9b`.
* **The image is rejected:** use a PNG or JPEG. HEIC photos from an iPhone need Round 2's improvement; until then, take a screenshot of the photo.
* **Fields are left blank:** that's intended when the image doesn't clearly show something, such as the year or time zone. Read the app's notes and fill them in yourself.
* **The first extraction is slow:** the model takes a moment to load. Later extractions are faster.
* **Your laptop slows to a crawl or freezes:** AI models running on your laptop need a lot of memory, and older laptops can struggle. Close other apps first. If that doesn't help, ask Claude: "My laptop is struggling. Please switch the app to the smaller qwen3.5:4b model and update the guides." Or ask a lab proctor for a lab PC.
* **"Port 8503 is already in use":** the app is probably already running in another terminal window. Stop that one with **Control + C**, or use the one that's running.
* **Anything else:** copy the error message into Claude and ask for help, as in the example above.

<br>

## Key Takeaways

In this lab, you gave Claude a picture as well as a prompt, and worked with an AI model that can read images. You also saw why a human review step matters: a blank field is better than a wrong one, and nothing is exported until you've checked and confirmed it.

Congratulations! You've built three working apps with AI: a Knowledge Base, an Action Center, and now an Image-to-Calendar assistant. Along the way, your Claude session has become "context rich": it knows what you've built and how you like to work. That makes it a great starting point for your own project, such as a fitness tracker or a portfolio tracker.

From here, you can:

* **Keep improving this app** with the optional sections below, or
* **Start your own project** in the same Cowork session, with [Lab 04 — Build Your Own Project](Lab_04_Guide_Build_Your_Own_Project.html).

<br>

## Optional: Improve It

Choose your route:

* **Guided route:** work through the three development prompts below, one at a time.
* **Creative route — bonus challenge!** Write your own instructions. Try your own layout, workflow, and improvement ideas. For extra points, show what you changed, why it helps, and the experiment you used to test it. Keep local processing, editable details, and human confirmation before export in your design.

Both routes follow the same pattern: predict the result, try it, compare what happened, and improve one thing. Don't paste all three prompts at once. Pick one round, or do them in order.

| Round | Your activity | Checkpoint |
| --- | --- | --- |
| Round 1: Broaden the idea | Try a whole conference and a single session | Incomplete events remain editable suggestions. |
| Round 2: Try real-world inputs | Photograph handwriting and try HEIC | The image opens; uncertain readings are visible. |
| Round 3: Improve the handoff | Test filenames, edits, and calendar import | The file uses the current confirmed details. |

Work alone or in pairs. In pairs, one person operates the app while the other compares every field with the image; switch roles after each round.

### Round 1: What Counts as an Event?

An event might be an entire conference, a one-hour session, or a save-the-date announcement without times. Test whether your first version handles that variety.

**Predict and try:** Create a simple image saying “Community Tech Days — October 5–8, 2026 — Austin & Virtual — Save the date.” A screenshot of text you type is enough. Separately, create a session image saying “Design session — October 6, 2026 — 14:00–15:00 UTC.” Before extracting, decide how many events each image should produce and which fields should remain blank.

#### Development Prompt 1: Expand the Event Types

> Improve my existing Image to Calendar app so it can suggest a whole multi-day event, a save-the-date announcement, or an individual session. First inspect what already works and use my test observations: [replace this with what happened and what you expected].
>
> A conference flyer with an explicit date range is an event even without an agenda or clock times. Preserve the first and last dates as one spanning event. Keep missing times and time zone blank, with timing marked Not specified. Let me choose an all-day calendar hold during review or enter verified times. Don't automatically call it all-day because times are missing. Use the inclusive last day in the editor and the correct exclusive end date in the .ics file.
>
> If an image lists separate sessions, suggest them separately and let me select one at a time, up to eight suggestions. Changing the selection must clear confirmation. Don't invent sessions, duplicate one event for each day, or derive events from unrelated dates. Add focused tests, keep the original review protections, and update the Quickstart and Application Guide. Explain what I should try to verify this change.

**Checkpoint:** The conference should produce one suggestion spanning October 5–8 with no invented times. Choose **All-day event**, confirm, and import: it should cover all four days, with no event on October 9. The session should have its own single date and timed details. For an extra challenge, combine two separately timed sessions into one image and check selection and review.

**Discuss:** What is the difference between extracting dates from a flyer and choosing how you want to block time on your calendar?

### Round 2: Can It Handle a Photo of Your Notes?

**Predict and try:** Handwrite a fictional event with a full date, start/end times, and time zone. Photograph it straight on in good light. Make a second version with the year deliberately omitted or one time unreadable. Exchange photos with a partner if possible and record what a human can confidently read before testing the model.

If your phone saves HEIC photos, try one directly. Otherwise, use PNG/JPEG for handwriting and mark the HEIC check as not tested; renaming a file extension does not convert its format.

#### Development Prompt 2: Support Handwriting and Phone Photos

> Improve the existing app for handwritten notes, cursive, whiteboards, mixed annotations, and HEIC/HEIF phone photos. My observations are: [replace with the image type, what I could read, and what the app returned]. Inspect existing support before changing it.
>
> Use a local HEIC decoder such as pillow-heif, preserve image orientation, and convert to a model-compatible image in memory. Accept .heic and .heif uploads, validate actual file content, accept photos up to 50 MB and 80 megapixels and automatically resize large photos to at most 3200 pixels on the longest side without changing their aspect ratio or the original file, and use the primary photo when a HEIF container holds multiple images. Show an actionable error if decoding fails.
>
> Tell the vision model to read handwriting as event evidence. Leave unclear fields blank, flag conflicting corrections, and mark unreadable transcription as [illegible]. Don't guess a missing year or ambiguous digit. Keep manual editing and confirmation. Add tests using real encoded HEIC data for conversion and mocked responses for uncertain fields; explain that these tests don't prove handwriting accuracy. Update dependencies, the start file, and the Quickstart and Application Guide, then tell me how to restart and test the change.

**Checkpoint:** A supported HEIC photo should preview and reach extraction without manual conversion. Try a full-resolution phone photo if available: a 24- or 48-megapixel image should resize automatically instead of being rejected. Check that the preview is upright and its text is still readable; upload a closer crop if small details are lost. After adding the decoder, stop the app and double-click the start file again: it reinstalls the dependencies and restarts the app. Restart after changing the upload limit too, so the uploader accepts files up to 50 MB. Check that a missing year remains blank. Compare the handwritten suggestions with the actual photo, including anything the model failed to flag.

**Discuss:** Did changing lighting or legibility help? Was a failure caused by opening the image, reading its text, or interpreting the event? Those are different problems and call for different follow-up instructions.

### Round 3: Make the Result Easy to Use and Verify

**Predict and try:** Confirm an event, then change its title or start time. Try downloading again. Also inspect the downloaded filename and import the file into your calendar. Write down one point where a participant might get confused.

#### Development Prompt 3: Improve the Calendar Handoff

> Improve the existing app's review and download experience based on this observation: [replace with the confusing behavior and your desired result]. Inspect current behavior before changing it.
>
> Name the downloaded .ics file after the confirmed event title, replacing characters unsuitable for filenames and shortening long names. The calendar entry must also use the confirmed title. For example, Community Tech Days should download as Community Tech Days.ics.
>
> Make the preview, review checkbox, confirmation, and download clearly reflect the current details. Any edit, event selection, source change, or new extraction must remove the old approval and download until I review and confirm again. Repeated downloads of one confirmation should have identical contents. Explain that importing a newly confirmed version may create a duplicate and that attendees can be added in the calendar app after import.
>
> Run relevant existing checks and add regression coverage if you find a broken review/export behavior. Update the Quickstart and Application Guide with the final workflow and explain how I can verify both the downloaded file and the imported event.

**Checkpoint:** The sample should now download as `Build with AI Workshop.ics`. Change the title and confirm again: both the new filename and imported event title should reflect your edit. Change a time after confirming: the old download should disappear. Remove duplicate test imports when you're done.

**Discuss:** What should count as “confirmed” when a person changes a field? Which details must be checked in the calendar app rather than just in the preview?

### Keep a Small Experiment Log

Fill this in as you work. A failed experiment with a clear explanation is useful lab evidence.

| Experiment | Expected result | Actual result | One change to try | Retest result |
| --- | --- | --- | --- | --- |
| Sample timed event | | | | |
| Multi-day announcement | | | | |
| Handwriting / HEIC | | | | |
| Edit after confirmation | | | | |

Before sending a development prompt, replace its bracketed placeholder with your observation. Include an error message if there is one. Ask for one focused change, then repeat the same test image to see whether that change helped. Re-extract after changing model instructions; an old suggestion won't update itself.

<br>

## Optional: When an Experiment Fails

A failure is useful evidence for your next iteration. You don't need to know the answer before asking your coding assistant for help, but you do need to describe what happened and check its proposed explanation.

**A real example from this project:** A phone photo was rejected by the app's 20-megapixel limit. We changed the app to resize large photos automatically. The next attempt reached Ollama but returned HTTP 400. The initial message only said to check logs and model support. The log supplied the missing evidence: **the request needed 5470 tokens, but the active context held only 4096**.

A context window is how much input and output the model can work with in a request. Images also use tokens. An image can fit the app's file-size limit yet exceed the model's context. In this case, the next change was to request a 16384-token context and show Ollama's specific error in the interface. A longer timeout would allow more waiting but would not create more context space. Other HTTP 400 responses can have different causes.

### Activity: Observe, Explain, Change, Retest

Use a failure you encounter, or discuss the example above if your app is working. Don't deliberately break a working installation just to reproduce it.

1. **Observe:** Record the action, image format and dimensions, selected model, and exact error. Note whether the image preview appeared before extraction failed.
2. **Locate the failing step:** Is the problem in upload/decoding, the Ollama request, interpreting the returned fields, or calendar export? Ask your coding assistant to inspect the relevant code and error details before suggesting a fix.
3. **Form a hypothesis:** Write “I think ___ failed because ___; the evidence is ___.” For the example, distinguish a model that cannot read images from a request that doesn't fit its context.
4. **Choose one change:** State what result would support your hypothesis. Replace the observations placeholder in the relevant development prompt with this evidence. Ask the assistant to implement the smallest justified fix, keep human review, add a regression check where useful, and update the Quickstart and Application Guide.
5. **Retest:** Run the same image and model again, then a known-good sample. Record whether the error disappeared and whether the returned dates and times are correct. A successful HTTP request alone isn't proof of correct extraction.

In pairs, have one person propose the explanation and the other identify the evidence that would confirm or challenge it. If the explanation is still uncertain, record it as a hypothesis rather than a fact.

| Observation | What it tells you | Next useful check |
| --- | --- | --- |
| App rejects the image before preview | The image has not reached the model. | File format, dimensions, decoder, and upload limits. |
| HTTP 400 after clicking Extract | Ollama rejected a request; the status alone doesn't explain why. | Server explanation and the matching log entry. |
| Error explicitly says input exceeds context | The request doesn't fit the active model context. | Request context setting, input size, and available memory. |
| Request succeeds but the date is wrong | Transport worked; recognition or interpretation still needs review. | Compare source text and warnings with the image. |

If you hit a context error, ask Claude to raise the model's context size and to show Ollama's full error message in the app, then restart the app before retesting. More context uses more memory. On a Mac, the recent log can be read with `tail -n 80 ~/.ollama/logs/server.log`. If Ollama was started with `ollama serve`, its terminal output is another source of evidence.

**Checkpoint:** Explain what failed, what evidence supported your change, what you retested, and what remains uncertain. If a new error appears at a later stage, record that separately—it may reveal the next problem rather than mean the previous fix failed.

<br>

## Optional: Final Checks and Share Back

Run the automated checks from your project folder:

```sh
uv run pytest
```

Tests show that particular behaviors work for known inputs. Mocked responses and the offline review demo don't prove that a model can read your images. Keep real extraction and calendar import checks in your experiment log too.

Use this short checklist before calling your version ready:

* ☐ One clear timed event completes the full workflow and imports correctly.
* ☐ Missing required details block confirmation rather than being silently filled in.
* ☐ An end before the start is rejected.
* ☐ Changing a confirmed field removes the old download.
* ☐ Each improvement I attempted has a recorded before/after result.
* ☐ The Application Guide describes the app I actually built, including known limitations.

With a partner or the group, show one image and the resulting calendar entry. Explain one thing the AI did well, one thing you corrected, and the prompt change that helped. If a feature remains untested or unreliable, say so.

<br>

## Optional: Going Further

You now have a working MVP. Choose one of the challenges below to develop next, based on a difficulty you observed. **These are optional projects.** You don't need to complete them to finish the lab.

### 1. Add a Date-Validation Section

A ticket might say **“Tuesday, September 23, 2026”**, but September 23, 2026 is actually a **Wednesday**. The text can be transcribed correctly and still contain a contradiction.

Design a validation section that displays the weekday printed on the ticket, the extracted calendar date, and the weekday calculated from that date using code. Highlight a mismatch and ask the user to resolve it before confirming. Preserve the source wording so the user can see what was compared. If the year or weekday is missing or unreadable, show that the comparison cannot be completed; don't invent it.

Your app may already check that dates exist, and you can ask the model to flag conflicting weekdays. This challenge adds an explicit weekday comparison in code and a dedicated review section, so it doesn't depend only on the model noticing the conflict.

**Try it:** Compare tickets saying “Tuesday, September 23, 2026” and “Wednesday, September 23, 2026.” The first should show a mismatch; the second should pass the weekday check. Then remove the year and check that the app asks for clarification. Edit the date and verify that the check runs again and clears the old confirmation.

**Discuss:** Which is wrong—the printed weekday or the numeric date? Calendar arithmetic can detect the inconsistency, but it cannot determine the organizer's intended date. Let the user verify with the organizer rather than silently moving the event to a Tuesday. A matching weekday also doesn't prove that a ticket is valid or the event details are current.

### 2. Distinguish the Event Date from Other Dates

A ticket or flyer may include an event date, a registration deadline, and a purchase date. Design a review area that labels what each date refers to and shows its supporting source text. Let the user choose which occasion belongs on the calendar. A registration reminder should be a deliberate choice with its own review, not silently replace the event.

**Try it:** Create a flyer that says “Purchased September 1, 2026 · Register by September 20, 2026 · Workshop September 23, 2026, 14:00–15:00 UTC.” The workshop suggestion should use September 23. Make one label unreadable and check that the app asks for clarification instead of selecting whichever date appears first.

**Discuss:** What evidence connects a date to an event? How would you make that connection visible to someone reviewing the suggestion?

### 3. Add a Crop-and-Retry Tool

Large phone photos may contain a small ticket surrounded by a table, wall, or other text. Add a crop control so users can select the relevant area before another extraction. Keep the full source available for comparison, and clear old suggestions and confirmation when the crop changes. Your first version resizes large images but does not provide an interactive crop tool.

**Try it:** Photograph a handwritten event from a distance. Compare extraction from the full photo with extraction from a crop of the event details. Check whether small text becomes easier to read. Then crop out the year deliberately: the app should report it as missing, rather than carry it over from an earlier result.

**Discuss:** Did cropping improve accuracy, and what useful context did it remove? How will users know which image produced the current suggestion?

### 4. Keep Separate Drafts for Multiple Sessions

If your app lets users select among suggestions, edits are probably not retained separately when switching events. Add a draft for each session so someone can review a full agenda without losing corrections. Track confirmation separately for each draft and keep export tied to the selected, confirmed version.

**Try it:** Use an image with two sessions. Correct the room for session A, switch to B and correct its time, then return to A. Both changes should survive. Confirm A, edit B, and verify that each draft's confirmation and download stay associated with the correct session. Decide what should happen to drafts when a new image replaces the agenda.

**Discuss:** Which state belongs to one event and which belongs to the whole upload? If you later save drafts across restarts, how will users find and delete them?

### Plan Your Next Experiment

Before asking AI to implement your idea, write three sentences: who it helps, what should change, and how you'll check it. Keep human review and confirmation in the workflow, and update the guides and relevant checks as the app evolves.

You can take the project home and use your own images. The skill to practice is the same: describe a useful first version, observe its behavior, and turn that evidence into the next improvement.

<br>

## What's Next

* **Next:** you've finished all three labs! Your Claude session now knows what you've built and how you like to work, so it's a great place to start your own project with [Lab 04 — Build Your Own Project](Lab_04_Guide_Build_Your_Own_Project.html). Or go back to the [Main Menu](https://gcodekhanna1.github.io/2026-10-ai-skills-lab/) to revisit any lab.
* **Before you leave:** see [How to Save Your Work for Later](Lab_Save_Your_Work.html), so you can pick up where you left off.
