# Operating Systems Lab Assignments

This repository contains all Operating Systems Lab Assignments completed as part of the ENCS351 – Operating Systems Laboratory course. Each assignment covers essential OS concepts, including process management, system calls, memory management, scheduling algorithms, IPC, and system-level simulations.

## 📂 Repository Structure

| Folder / File | Description |
|---------------|-------------|
| `Assignment1/` | Contains Task 1–5 demonstrating process creation using fork(), exec(), zombie & orphan process simulation, /proc inspection, and priority scheduling using nice() |
| `Assignment2/` | Contains system startup simulation using multiprocessing, inter-process logging, process execution simulation, and concurrent system tasks |
| `Assignment3/` | Contains memory management algorithms and priority CPU scheduling including Priority Scheduling, First Fit/Best Fit/Worst Fit memory allocation, MFT & MVT Memory Management Simulation |
| `Assignment4/` | Contains batch processing simulation, system startup simulation, system calls (fork, exec, pipe) & IPC, VM detection script, and shell script to display system information |
| `Scheduling/` | Contains CPU Scheduling Algorithms: FCFS, SJF, SRTF, Round Robin |
| `ASSIGNMENT1.OS.pdf` | Report for Assignment 1 |
| `ASSIGNMENT2.OS.pdf` | Report for Assignment 2 |
| `Assignment3_OS.pdf` | Report for Assignment 3 |
| `Assignment4_OS.pdf` | Report for Assignment 4 |
| `Scheduling.OS.pdf` | Report for CPU Scheduling Assignment |
| `README.md` | Documentation of all assignments |

## 🚀 Assignment Overview
### 📝 Assignment 1 — Process Management

**Includes:**
- Process creation using os.fork()
- Parent-child relationship
- Zombie process creation
- Orphan process creation
- Executing commands using os.execvp()
- Reading process information using /proc
- Using nice() for priority scheduling

**Run:**
```bash
cd Assignment1
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
python3 task5.py
```

### 📝  Assignment 2 — System Startup & Process Simulation

**Includes:**
- System Boot Simulation
- Process Creation & Task Execution
- Logging System**

**Run:**
```bash
cd Assignment2
python3 subtask1.py
python3 subtask2.py
python3 subtask3.py
python3 subtask4.py
```

### 📘 Assignment 3 — CPU Scheduling & Memory Management

**Includes:**
- Priority Scheduling
- First Fit, Best Fit, Worst Fit (Memory Allocation)
- MFT (Multiprogramming with Fixed Tasks)
- MVT (Multiprogramming with Variable Tasks)

**Run:**
```bash
python3 task1.py
```

### 📘 Assignment 4 — System Calls, IPC, VM Detection & Shell Scripting

**Includes:**
- Batch Processing Simulation  
- System Startup Simulation (Multiprocessing)  
- System Calls: `fork()`, `exec()`, `pipe()`  
- Inter-Process Communication (IPC)  
- Virtual Machine Detection using Python  
- System Information Shell Script  

**Run:**
```bash
python3 task1.py
```

### 📘 CPU Scheduling Algorithms — Scheduling Folder

**Includes:**
This section contains implementations of the four major CPU Scheduling Algorithms used in Operating Systems.  
Each script computes:
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)
- Average TAT and WT
- Gantt Chart order (implicitly through execution order)
These programs simulate how real OS schedulers allocate CPU time to processes.

**Run:**
```bash
python3 fcfs.py
