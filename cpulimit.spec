Summary:	CPU usage limiter
Summary(pl):	Ograniczanie wykorzystania procesora
Name:		cpulimit
Version:	1.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cpulimit/%{name}-%{version}.tar.gz
# Source0-md5:	f4ff6d4bfaef1258e8f5cd2041e2e2a3
Source1:	%{name}.1
URL:		http://cpulimit.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpulimit is a simple program that attempts to limit the cpu usage of a
process (expressed in percentage, not in cpu time). This is useful to
control batch jobs, when you don't want they eat too much cpu. It does
not act on the nice value or other scheduling priority stuff, but on
the real cpu usage. Also, it is able to adapt itself to the overall
system load, dynamically and quickly.

%description -l pl
cpulimit to prosty program ograniczaj�cy zu�ycie procesora przez
proces (wyra�one w procentach, nie w czasie). Jest to przydatne to
kontrolowania zada� wsadowych, �eby nie wykorzystywa�y zbyt du�o mocy
procesora. Program ten nie operuje na warto�ci nice czy innych
priorytetach kolejkowania, ale na rzeczywistym czasie dzia�ania.
Program jest te� w stanie dynamicznie dostosowa� si� do obci��enia
systemu.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} cpulimit.c -o cpulimit -lrt

%install
rm -rf $RPM_BUILD_ROOT
install -D cpulimit $RPM_BUILD_ROOT%{_bindir}/cpulimit
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/cpulimit.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/cpulimit.1*
