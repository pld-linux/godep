Summary:	Dependency tool for go
Name:		godep
Version:	60
Release:	1
License:	BSD
Group:		Development/Building
Source0:	https://github.com/tools/godep/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	03194aeb9b4d22ea6201ef83163cda70
URL:		https://github.com/tools/godep
ExclusiveArch:	%{ix86} %{x8664} %{arm}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# go stuff
%define _enable_debug_packages 0
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%define import_path github.com/tools/godep

%description
Dependency tool for go.

%prep
%setup -q

install -d src/github.com/tools
ln -s ../../../ src/github.com/tools/godep

%build
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace
%gobuild -o bin/godep %{import_path}

%install
rm -rf $RPM_BUILD_ROOT
install -d -p $RPM_BUILD_ROOT%{_bindir}
install -p bin/godep $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.md Readme.md License
%attr(755,root,root) %{_bindir}/godep
