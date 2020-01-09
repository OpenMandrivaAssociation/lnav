Summary:	A curses-based tool for viewing and analyzing log files
Name:		lnav
Version:	0.8.5
Release:	1
License:	BSD
Group:		File tools
Url:		http://lnav.org
Source0:	http://lnav.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)

%description
The log file navigator is an enhanced log file viewer that takes
advantage of any semantic information that can be gleaned from
the files being viewed, such as timestamps and log levels. Using this
extra semantic information, it can do things like interleaving
messages from different files, generate histograms of messages over
time, and providing hotkeys for navigating through the file. It is
hoped that these features will allow the user to quickly and
efficiently zero in on problems.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install

%files
%doc LICENSE NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/lnav.1.xz
