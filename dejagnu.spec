Summary:	A front end for testing other programs.
Summary(pl):	Platforma do testowania innych programów.
Name:		dejagnu
Version:	1.4.0
Release:	1
License:	GPL
Source0:	ftp://ftp.gnu.org/gnu/dejagnu/%{name}-%{version}.tar.gz
Group:		Development/Tools
Requires:	tcl >= 8.0, expect >= 5.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.
DejaGnu has several purposes: to make it easy to write tests for any
program; to allow you to write tests which will be portable to any
host or target where a program must be tested; and to standardize the
output format of all tests (making it easier to integrate the testing
into software development).

%description -l pl
DejaGnu jest platform± bazuj±c± na Expect'ie i Tcl s³u¿±ca do testowania
innych programów. DejaGnu umo¿liwia ³atwe tworzenie testów do niemal 
dowolnego programu, uruchamiania ich na ró¿nych platformach sprzêtowych oraz
zapewnia jednolity format raportów z przebiegu testowania. 

%prep
%setup -q -n dejagnu-1.4

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_datadir}/dejagnu
install -d $RPM_BUILD_ROOT%{_prefix}/doc/dejagnu-%{version}
%{__make} DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/runtest
%attr(755,root,root) %{_datadir}/dejagnu/config.guess
%attr(755,root,root) %{_datadir}/dejagnu/runtest.exp
%attr(755,root,root) %{_datadir}/dejagnu/libexec/config.guess
%{_datadir}/dejagnu/[^crl]*
%{_datadir}/dejagnu/rlogin.exp
%{_datadir}/dejagnu/remote.exp
%{_datadir}/dejagnu/rsh.exp
%{_datadir}/dejagnu/libgloss.exp
%{_datadir}/dejagnu/config


# %config site.exp

%doc COPYING NEWS README AUTHORS INSTALL ChangeLog doc/overview
 
