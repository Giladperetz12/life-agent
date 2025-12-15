# Life Agent

A basic rule-based personal life management agent.

The agent analyzes personal data such as emails and calendar events,
decides what action to take, and runs autonomously using a basic agent loop.

This project focuses on agent-based design, clean architecture, and automation
logic — without using external APIs or complex AI models.

## Project Overview
The agent:
- Reads data from local JSON files
- Analyzes the current state
- Decides what action to take based on predefined rules
- Executes the selected action
- Sleeps and repeats the process

--

## Core Features
Mail Agent : loads emails data from a JSON file, count unread and important emails, prioritizes important emails over regular unread emails, display summaries accordignly
Calendar Agent : loads calendar events from a JSON file, detects overlapping events (conflicts), gives calendar conflicts top priority in agent decisions
Periodic Agent Loop : runs automatically every fixed interval (configurable), executes the full agent cycle repeatedly, can be stopped gracefully by the user

## Agent Decision Logic : Priority Order
1. Calendar conflicts detected → show calendar conflicts
2. Important emails exist → show important emails
3. Unread emails exist → show mail summary
4. No action needed → idle



