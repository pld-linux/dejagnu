Summary:	A front end for testing other programs
Summary(pl):	Platforma do testowania innych programów
Name:		dejagnu
Version:	1.4.0
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/dejagnu/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	tcl >= 8.0
Requires:	expect >= 5.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.
DejaGnu has several purposes: to make it easy to write tests for any
program; to allow you to write tests which will be portable to any
host or target where a program must be tested; and to standardize the
output format of all tests (making it easier to integrate the testing
into software development).

%description -l pl
DejaGnu jest platform± bazuj±c± na Expect'ie i Tcl s³u¿±ca do
testowania innych programów. DejaGnu umo¿liwia ³atwe tworzenie testów
do niemal dowolnego programu, uruchamiania ich na ró¿nych platformach
sprzêtowych oraz zapewnia jednolity format raportów z przebiegu
testowania.

%prep
%setup -q -n dejagnu-1.4
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
cd example/calc
rm -f missing
aclocal
autoconf
automake -a -c -f
cd ../..
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d$RPM_BUILD_ROOT{%{_datadir}/dejagnu,%{_prefix}/doc/dejagnu-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %config site.exp
%doc *.gz doc/overview
%attr(755,root,root) %{_bindir}/runtest
%dir %{_datadir}/dejagnu
%attr(755,root,root) %{_datadir}/dejagnu/config.guess
%attr(755,root,root) %{_datadir}/dejagnu/runtest.exp
%attr(755,root,root) %{_datadir}/dejagnu/libexec/config.guess
%{_datadir}/dejagnu/[^crl]*
%{_datadir}/dejagnu/rlogin.exp
%{_datadir}/dejagnu/remote.exp
%{_datadir}/dejagnu/rsh.exp
%{_datadir}/dejagnu/libgloss.exp
%{_datadir}/dejagnu/config
