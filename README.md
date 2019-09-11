# boilerplate-digdag-py

sample to poll folder to get file list with python script called from digdag

## install digdag

1. run the following command on command prompt
2. modify PATH with addign "%USERPROFILE%\bin"

```sh
PowerShell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::TLS12; mkdir -Force $env:USERPROFILE\bin; Invoke-WebRequest http://dl.digdag.io/digdag-latest.jar -OutFile $env:USERPROFILE\bin\digdag.bat}"
```

## how to run

### one time
  
```sh
cd <project folder folder>
digdag run mydag.dig
```

### scheduled
  
```sh
cd <project folder folder>
digdag scheduler
```

if you want to change interval to run digdag tasks, you should change operator and its parameter at schedule task in mydag.dig. you can refer to this page, [Scheduling workflow](https://docs.digdag.io/scheduling_workflow.html), about how to set shedule.

```yaml
...
schedule:
  minutes_interval>: 1
...
```

## reference
- [Digdag official document](https://docs.digdag.io/index.html)