# kill a process quickly

lsof -t -i :5000

- lsof = "List Open Files."
In Unix/Linux, everything (including network sockets) is treated as a file.
- -i :5000 = Show processes using network port 5000.
- -t = Only print the process ID (PID) without extra details.

kill -9
- kill sends a signal to terminate a process.
- -9 = SIGKILL = force kill (process can’t ignore it).
- Used when normal kill doesn’t stop the process.

Complete command : kill -9 $(lsof -t -i :5000)
