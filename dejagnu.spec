Summary:	A front end for testing other programs
Summary(pl.UTF-8):	Platforma do testowania innych programów
Name:		dejagnu
Version:	1.4.4
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/dejagnu/%{name}-%{version}.tar.gz
# Source0-md5:	053f18fd5d00873de365413cab17a666
Patch0:		%{name}-ac_fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	tcl >= 8.0
Requires:	expect >= 5.21
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.
DejaGnu has several purposes: to make it easy to write tests for any
program; to allow you to write tests which will be portable to any
host or target where a program must be tested; and to standardize the
output format of all tests (making it easier to integrate the testing
into software development).

%description -l pl.UTF-8
DejaGnu jest platformą bazującą na Expect'ie i Tcl służąca do
testowania innych programów. DejaGnu umożliwia łatwe tworzenie testów
do niemal dowolnego programu, uruchamiania ich na różnych platformach
sprzętowych oraz zapewnia jednolity format raportów z przebiegu
testowania.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %config site.exp
%doc NEWS README AUTHORS ChangeLog doc/overview.* doc/README.Writers doc/ref* doc/user* doc/dejagnu* doc/html
%attr(755,root,root) %{_bindir}/runtest
%dir %{_datadir}/dejagnu
%attr(755,root,root) %{_datadir}/dejagnu/runtest.exp
%dir %{_datadir}/dejagnu/libexec
%attr(755,root,root) %{_datadir}/dejagnu/libexec/config.guess
%{_datadir}/dejagnu/[^crl]*
%{_datadir}/dejagnu/rlogin.exp
%{_datadir}/dejagnu/remote.exp
%{_datadir}/dejagnu/rsh.exp
%{_datadir}/dejagnu/libgloss.exp
%{_datadir}/dejagnu/config
%{_mandir}/man1/*
%{_includedir}/dejagnu.h
