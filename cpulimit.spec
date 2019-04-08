Summary:	CPU usage limiter
Summary(pl.UTF-8):	Ograniczanie wykorzystania procesora
Name:		cpulimit
Version:	2.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/limitcpu/limitcpu/%{name}-%{version}.tar.gz
# Source0-md5:	008b012636007e954de3d5a50b83e540
URL:		http://limitcpu.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpulimit is a simple program that attempts to limit the cpu usage of a
process (expressed in percentage, not in cpu time). This is useful to
control batch jobs, when you don't want they eat too much cpu. It does
not act on the nice value or other scheduling priority stuff, but on
the real cpu usage. Also, it is able to adapt itself to the overall
system load, dynamically and quickly.

%description -l pl.UTF-8
cpulimit to prosty program ograniczający zużycie procesora przez
proces (wyrażone w procentach, nie w czasie). Jest to przydatne to
kontrolowania zadań wsadowych, żeby nie wykorzystywały zbyt dużo mocy
procesora. Program ten nie operuje na wartości nice czy innych
priorytetach kolejkowania, ale na rzeczywistym czasie działania.
Program jest też w stanie dynamicznie dostosować się do obciążenia
systemu.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} -D LINUX cpulimit.c -o cpulimit -lrt -lpthread

%install
rm -rf $RPM_BUILD_ROOT
install -D cpulimit $RPM_BUILD_ROOT%{_bindir}/cpulimit
install -D cpulimit.1 $RPM_BUILD_ROOT%{_mandir}/man1/cpulimit.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/cpulimit.1*
