# overview
An introduction code as I pick up the C# journey.

1. Create a new C# project

In your terminal:
 $ mkdir your_project_folder && cd your_project_folder
 $ dotnet new console
   That creates a Program.cs file and a number of other files

2. Run the program

In your project folder: $ dotnet run

# Files

All those files and folders you see in your .NET project aren’t random, they’re the build artifacts and metadata that .NET uses to compile, run, and manage dependencies. 

Let’s break them down:

amaseghe@black-panther:~/developer/c#/example$ tree
.
├── bin  <--- binary output. These files are generated when you build or run. Even you delete, it's ok, they'll be always rebuilt whenever a build/run happens.
│   └── Debug
│       └── net8.0            → Contains compiled binaries for your project in Debug mode targeting .NET 8.0.
│           ├── example       → A platform-specific launcher/executable (so you can run without typing dotnet example.dll).
│           ├── example.deps.json → Lists dependencies and how they’re resolved.
│           ├── example.dll      → Your compiled program in .NET Intermediate Language (IL).
│           ├── example.pdb      → Debug symbols (lets you debug in VS Code).
│           └── example.runtimeconfig.json → Tells the .NET runtime which version to use (net8.0).
├── example.csproj      → The project file. It tells .NET which framework to target (net8.0), dependencies (NuGet packages), and build settings.
├── obj           --> Temporary files used by the compiler/MSBuild.Think of it like scratch space during builds.
│   ├── Debug
│   │   └── net8.0
│   │       ├── apphost
│   │       ├── example.AssemblyInfo.cs    → Auto-generated metadata (version, attributes).
│   │       ├── example.AssemblyInfoInputs.cache
│   │       ├── example.assets.cache
│   │       ├── example.csproj.CoreCompileInputs.cache
│   │       ├── example.csproj.FileListAbsolute.txt
│   │       ├── example.dll
│   │       ├── example.GeneratedMSBuildEditorConfig.editorconfig → Generated code style/build rules.
│   │       ├── example.genruntimeconfig.cache
│   │       ├── example.GlobalUsings.g.cs
│   │       ├── example.pdb
│   │       ├── ref             --> ref/ & refint/ → Reference assemblies (used for compilation, not execution).
│   │       │   └── example.dll
│   │       └── refint
│   │           └── example.dll
│   ├── example.csproj.nuget.dgspec.json
│   ├── example.csproj.nuget.g.props
│   ├── example.csproj.nuget.g.targets
│   ├── project.assets.json       → Dependency graph (NuGet packages).
│   └── project.nuget.cache       → Speed up incremental builds (so dotnet build doesn’t recompile everything every time).
├── Program.cs         → Your actual C# source code (the entry point).
└── README.md          → Just a documentation file (optional, for you).

9 directories, 26 files
amaseghe@black-panther:~/developer/c#/example$

#  How they all connect
1. You write Program.cs.
2. dotnet build compiles it → creates intermediate stuff in obj/.
3. Then it links everything into the final output → goes into bin/.
4. dotnet run just executes the compiled binary in bin/Debug/net8.0/.

👉 In practice:
- You edit Program.cs & .csproj.
- You can usually ignore bin/ and obj/ — they’re auto-generated, safe to delete (they’ll be rebuilt).

# C# version?
There are a few ways you can check which C# version you’re using, depending on your environment (since C# version is tied to the .NET SDK installed).

✅ Option 1: Check via CLI (dotnet SDK)
 $ dotnet --version

This tells you the .NET SDK version. Each SDK corresponds to a C# version.

| .NET SDK Version | Default C# Version |
| ---------------- | ------------------ |
| .NET 8.x         | C# 12              |
| .NET 7.x         | C# 11              |
| .NET 6.x (LTS)   | C# 10              |
| .NET 5.x         | C# 9               |
| .NET Core 3.x    | C# 8               |



✅ Option 2: Check in a C# Project 

Inside a project folder, open the .csproj file and look for:

 <TargetFramework>net8.0</TargetFramework>

That tells you the framework version (e.g., net8.0 → .NET 8 → C# 12).

You can use this file to force a specific C# version for your project : 

Inside your project’s .csproj, you can add:
<PropertyGroup>
  <LangVersion>12.0</LangVersion>
</PropertyGroup>

This overrides the default (useful if you want to use preview features).


✅ Option 3: Check all installed SDKs

  $ dotnet --list-sdks

This shows every .NET SDK you have installed, e.g.:

6.0.412 [/usr/share/dotnet/sdk]
7.0.306 [/usr/share/dotnet/sdk]
8.0.100 [/usr/share/dotnet/sdk]

# C# Access Strings & Find position(index)
You can access the characters in a string by referring to its index number inside square brackets [].

This example prints the first character in myString:

string myString = "Hello";
Console.WriteLine(myString[0]);  // Outputs "H"
Console.WriteLine(myString[1]);  // Outputs "e"

You can also find the index position of a specific character in a string, by using the IndexOf() method:

string myString = "Hello";
Console.WriteLine(myString.IndexOf("e"));  // Outputs "1"

# Special Characters & Escape Character

Because strings must be written within quotes, C# will misunderstand this string, and generate an error:

string txt = "We are the so-called "Vikings" from the north.";

The solution to avoid this problem, is to use the backslash escape character.

The backslash (\) escape character turns special characters into string characters:

// The sequence \" inserts a double quote in a string:
string txt = "We are \"Vikings\" from the north."; 

// The sequence \'  inserts a single quote in a string
string txt = "It\'s alright."; 

// The sequence \\  inserts a single backslash in a string:
string txt = "The character \\ is called backslash.";


