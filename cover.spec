{incl_app, periodic, details}.
%{excl_mods, com, []}.
%{incl_dirs_r, ["src", "test"]}.
%{src_dirs, com, ["src", "test"]}.
{include, ["src", "include"]}.

%% List of Nodes on which cover will be active during test.
%% Nodes = [atom()]
%{nodes, Nodes}.

%% Files with previously exported cover data to include in analysis.
%% CoverDataFiles = [string()]
%{import, CoverDataFiles}.

%% Cover data file to export from this session.
%% CoverDataFile = string()
%{export, CoverDataFile}.

%% Cover analysis level.
%% Level = details | overview
%{level, Level}.

%% Directories to include in cover.
%% Dirs = [string()]
%{incl_dirs, Dirs}.

%% Directories, including subdirectories, to include.
%{incl_dirs_r, Dirs}.

%% Specific modules to include in cover.
%% Mods = [atom()]
% {incl_mods, Mods}.

%% Directories to exclude in cover.
%{excl_dirs, Dirs}.

%% Directories, including subdirectories, to exclude.
%{excl_dirs_r, Dirs}.

%% Specific modules to exclude in cover.
% {excl_mods, Mods}.

%% Cross cover compilation
%% Tag = atom(), an identifier for a test run
%% Mod = [atom()], modules to compile for accumulated analysis
% {cross,[{Tag,Mods}]}.