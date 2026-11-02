# CSE316 — Process Monitoring and Management Dashboard

## Project overview

This project is a web dashboard for monitoring Linux processes in real time. It shows CPU usage, memory usage, process states, and a live desktop view. It also allows an administrator to control a selected process.

## Team members

| Member | Contribution |
| --- | --- |
| Gokul Prasath | Backend connection, system setup, and desktop streaming |
| Swastik Das | Process monitoring, data collection, and control API |
| Bishal Sarkar | Dashboard design and frontend implementation |

## How it works

```text
Dashboard
   |
   +-- gets CPU, memory, and process data from the backend
   |
   +-- shows a live desktop through KasmVNC
   |
   +-- sends process-control actions to the backend
                                      |
                                      v
                              Linux process system
```

The dashboard refreshes process information every 1.5 seconds. When a user selects an action, the backend sends the required Linux signal to that process.

## Features

- Live CPU and memory charts
- Process table with PID, user, state, CPU use, memory use, and command
- Filters for all processes, high CPU processes, running processes, and zombies
- Sorting by CPU, memory, or PID
- Process details panel with the full command line
- Embedded KasmVNC desktop view
- Event log for alerts and process actions

## Process states

| Code | Meaning |
| --- | --- |
| `R` | Running |
| `S` | Sleeping or waiting |
| `T` | Stopped or paused |
| `Z` | Zombie process |

## Process actions

| Action | Signal | Result |
| --- | --- | --- |
| Terminate | `SIGTERM` | Requests a safe shutdown |
| Kill | `SIGKILL` | Stops the process immediately |
| Suspend | `SIGSTOP` | Pauses the process |
| Resume | `SIGCONT` | Continues a paused process |

## API

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/processes/` | `GET` | Returns system usage and the current process list |
| `/api/manage_process/` | `POST` | Controls a process using `pid` and `action` |

Available actions are `terminate`, `kill`, `suspend`, and `resume`.

## Screenshots

### CPU stress monitoring

![Dashboard showing live CPU stress processes and utilization](<images/Screenshot%202026-11-01%20at%204.58.43%E2%80%AFPM.png>)

### CPU stress test output

![Dashboard showing CPU stress test output in the remote desktop](<images/Screenshot%202026-11-01%20at%204.59.52%E2%80%AFPM.png>)

### Memory stress monitoring

![Dashboard showing live memory stress processes and utilization](<images/Screenshot%202026-11-01%20at%205.03.30%E2%80%AFPM.png>)

