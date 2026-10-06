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

# Lab 00 — Let's Get Started!

## Introduction

The goal of this document is to walk you through the steps of setting up the basics of what you'll need on your laptop to work on the lab.

* **All guides and materials:** [gcodekhanna1.github.io/2026-10-ai-skills-lab](https://gcodekhanna1.github.io/2026-10-ai-skills-lab/). Each guide is a web page, with a PDF version to print or save.

* **Before the workshop:** you can do Steps 01–03 at home on your own laptop, which saves time in the lab. Steps 04–07 are done in the lab, once you have your desk number.

<br>

## Your Path Through This Guide

Some steps are different on a lab PC, because they're already done for you. Look for the blue **🖥️ On a lab PC** boxes.

<table class="path">
<tr><th>Step</th><th>💻 On your own laptop</th><th>🖥️ On a lab PC</th></tr>
<tr><td>01 Create a folder for your lab files</td><td>Do it</td><td>Do it</td></tr>
<tr><td>02 Install the Claude desktop app</td><td>Install or update it</td><td class="skip"><b>Skip:</b> already installed</td></tr>
<tr><td>03 Install Ollama</td><td>Install it, then check it's running</td><td class="skip"><b>Don't install it:</b> just check it's running</td></tr>
<tr><td>04 Open your email</td><td>Do it</td><td class="skip"><b>Check Claude first:</b> skip if Claude is already signed in as your Demo number</td></tr>
<tr><td>05 Log into Claude</td><td>Do it</td><td class="skip"><b>Check first:</b> Claude may already be signed in as your Demo number</td></tr>
<tr><td>06 Start a Cowork session</td><td>Do it</td><td>Do it (start a new session)</td></tr>
<tr><td>07 Access Webex Messaging</td><td>Do it</td><td>Do it</td></tr>
</table>

<br>

## Overview of What You Need

* **Laptop or lab PC:** your choice. Use your own laptop, or a lab PC that already has the Claude desktop app and Ollama installed. Either way, you can take everything you build with you (see [How to Save Your Work for Later](Lab_Save_Your_Work.html)).

* **Organization account:** note your account for the lab, `demo-xy@paradigmventures.ai`, where **xy** is the number on your desk (for example, `demo-07@paradigmventures.ai`).
    - This will be your account for accessing other services throughout this lab.

* **Claude desktop app:** our main engine for building the lab, vibe coding, and asking questions.

* **Ollama:** a free, open-source platform that lets you download and run large language models (LLMs) directly on your own computer.

* **uv:** a fast, free tool that installs Python and the add-on libraries ("packages") each app needs, keeping every project's setup separate and tidy. You don't need to install it now: the start file Claude creates in Lab 01 installs it for you.

* **Email access:** a way to access one of your email accounts (either a work-related or personal account) to receive the verification link from Claude.

* **Web browser:** to access the Webex organization you'll be a part of (used in Lab 02, and so the lab team can send you files and help during the workshop).

* **Note:** you'll install a few free tools (the Claude desktop app and Ollama in Lab 00, and uv in Lab 01). If your work laptop doesn't allow installs, ask us for a lab PC.

<br>

## Step 01: Create a Folder for Your Lab Files

*✅ You can do this step before the lab on your own laptop.*

<p class="warning">⚠️ Make sure to create this folder in your computer's home folder (the folder with your user name). Do NOT create it in OneDrive, Dropbox, Box, Google Drive or iCloud Drive. We have found that the constant syncing of these cloud-based folders breaks the build. The Desktop or Documents folder is OK as long as it isn't being synced by a cloud service.</p>

* Create the folder in your **home folder** (the folder with your user name):
    - **Mac:** in Finder, press **⌘ + Shift + H**. Your home folder opens (e.g. `/Users/yourname`). Choose **File → New Folder**.
    - **Windows:** in File Explorer, click the address bar, type `%USERPROFILE%` and press **Enter**. Your home folder opens (e.g. `C:\Users\yourname`). Choose **New → Folder**.
    - Give it a name you'll recognize, such as `2026 - WebexOne - AI Skills Lab`.
    - This is the folder that will contain all the files and dependencies for what you will be building in this lab.

* **Why not a synced folder?** While Claude builds, it creates thousands of small files. A sync app trying to upload them at the same time can lock files and break the build. Desktop and Documents are often synced without you noticing (by iCloud on a Mac, or OneDrive on many work laptops), which is why we use your home folder.
    - **Quick check:** if the folder's location includes "OneDrive", "Dropbox", "Box", "Google Drive" or "iCloud", move it.

<br>

## Step 02: Install the Claude Desktop App

*✅ You can do this step before the lab on your own laptop.*

<p class="labpc"><b class="lead">🖥️ On a lab PC: nothing to do here.</b>Claude is already installed. Go straight to <b>Step 03</b>.</p>

* If you have not done so already, install the Claude desktop app from [claude.com/download](https://claude.com/download).
    - **Already have it?** Update it to the latest version before the lab.

* Double-click the installer file and follow the directions.

<br>

## Step 03: Install Ollama

*✅ You can do this step before the lab on your own laptop.*

<p class="labpc"><b class="lead">🖥️ On a lab PC: don't install Ollama, just check it.</b>Ollama is already installed. Skip to <b>Check That Ollama Is Running</b> below.</p>

* Download and install Ollama for your operating system from [ollama.com/download](https://ollama.com/download).

<br>
<p align="center">
  <img src="Lab_00_Ollama_Install_Screenshot.png" alt="Ollama install screenshot" width="60%">
</p>
<br>

### Check That Ollama Is Running

<p class="info"><b>You don't need an Ollama account.</b> If Ollama asks you to sign in or create an account, close that window: everything in this lab runs without one.</p>

* **Menu bar:** after installing, open the Ollama app. On a Mac, a small llama icon appears in the menu bar at the top right of your screen (on Windows, in the system tray near the clock). If you see it, Ollama is running.

* **Terminal:** you can also check from a terminal window, a text window where you type commands. You'll use it in every lab.
    - **Mac:** press **⌘ + Space**, type **Terminal**, and press **Return**.
    - **Windows:** click **Start**, type **PowerShell**, and press **Enter**.
    - Type the following command and press **Return** (or **Enter**):

```sh
ollama --version
```

* You should see a line like `ollama version is 0.x.x`. If you see `command not found` instead, open the Ollama app once and try again.

* Ollama starts with no AI models installed. Each lab will tell you which model to download when you need it. (On a lab PC, they're already downloaded.)

<br>

## Step 04: Open Your Email

*🏫 Do this step in the lab, once you have your desk number.*

<p class="labpc"><b class="lead">🖥️ On a lab PC: check Claude first.</b>Open Claude and look at the lower left corner. If it already shows your Demo number (for example, Demo-07), you're signed in: skip Steps 04 and 05 and go to <b>Step 06</b>. Otherwise, do this step.</p>

* **Why now:** when you log into Claude in the next step, Claude emails you a sign-in link. With your email already open, you can click it right away.

* Open the email account you registered for the workshop with (work or personal) **on this same computer**, in a web browser or your email app.
    - **Using a lab PC?** Sign in to your email in a web browser.

* Keep it open, and continue to Step 05.

<br>

## Step 05: Log Into the Claude Desktop App

*🏫 Do this step in the lab, once you have your desk number.*

<p class="labpc"><b class="lead">🖥️ On a lab PC: you may already be signed in.</b>If the lower left corner of Claude shows your Demo number, go to <b>Step 06</b>. If it shows a different Demo number, click it, choose <b>Log out</b>, and sign in with yours as described below.</p>

* Note your organization account email. It should have a format such as `demo-xy@paradigmventures.ai`.

* Use that to log into Claude (see the lower left corner of the application).

<br>
<p align="center">
  <img src="Lab_00_Claude_Login_Screenshot.png" alt="Claude desktop app login screen" width="40%">
</p>
<br>

* Go back to your email (from Step 04) and look for the verification link, which should look like the screenshot below. It can take a minute to arrive; if you don't see it, check your spam or junk folder. **Open the link on the same computer where you're running Claude.**
    - **Note:** the lab account forwards Claude's email to the address you registered with.
    - **Asked for a code?** Claude's screen may mention a code, but the email contains a sign-in **link** instead. Just click the link.

<br>
<p align="center">
  <img src="Lab_00_Claude_Verification_Screenshot.png" alt="Claude verification email with sign-in link" width="60%">
</p>
<br>

* Here is what your screen should look like once your email has been verified:

<br>
<p align="center">
  <img src="Lab_00_Claude_Initial_View_Screenshot.png" alt="Claude desktop app after logging in" width="80%">
</p>
<br>

<br>

## Step 06: Start a Cowork Session

*🏫 Do this step in the lab, once you have your desk number.*

<p class="labpc"><b class="lead">🖥️ On a lab PC: start a new session.</b>You may see sessions from an earlier participant in the sidebar. Ignore them, and start a <b>+ New</b> session with your own lab folder.</p>

* At the top right of the sidebar, make sure **Chat and Cowork** (the speech-bubble icon) is selected.

<br>
<p align="center">
  <img src="Lab_00_Claude_Chat_Cowork_Toggle_Screenshot.png" alt="The Chat and Cowork button selected at the top of the Claude desktop app sidebar, next to the Code button" width="50%">
</p>
<br>

* In the upper left corner, click the **+ New** button.
    - **Don't see it?** The sidebar may be hidden: click the sidebar icon at the top left to show it.

<br>
<p align="center">
  <img src="Lab_00_Claude_New_Session_Screenshot.png" alt="Claude desktop app when you start a new session" width="60%">
</p>
<br>

* Configure the session to be a Cowork session:
    - In the dialog box, select **Cowork** (instead of **Chat**).
    - Leave the default model as **Opus 5.5** (it is one of the latest models from Anthropic).
    - Click **Project or folder** and select the folder you created earlier (e.g., `2026 - WebexOne - AI Skills Lab`).
    - If Claude asks for permission to access the folder, click **Always Allow**.
    - Check that the folder is connected: its name should show in the session. If it doesn't, add it again.

* **Approval prompts:** as you work, Claude asks before some actions. Read the request, then click **Allow** (or **Allow for this task**, so it doesn't ask again for the same kind of action).

<br>

## Step 07: Access Webex Messaging

*🏫 Do this step in the lab, once you have your desk number.*

* **Why now:** you won't need Webex until Lab 02, but once you're signed in, the lab team can send you files and help directly in Webex if you get stuck.

* In your web browser, open a private (incognito) window and go to [web.webex.com](https://web.webex.com).

* Sign in with your organization email, `demo-xy@paradigmventures.ai`. The password is `Cisco123#`.

* You should see some Webex spaces with conversations already underway:

<br>
<p align="center">
  <img src="Lab_00_Webex_Spaces_Screenshot.png" alt="Webex spaces with conversations underway" width="60%">
</p>
<br>

<br>

## What's Next

* **Next:** you're all set up! Continue to [Lab 01 — Build Your Personal Knowledge Base](Lab_01_Guide_Knowledge_Base.html).
