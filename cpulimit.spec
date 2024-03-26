Summary:	CPU usage limiter
Summary(pl.UTF-8):	Ograniczanie wykorzystania procesora
Name:		cpulimit
Version:	3.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://downloads.sourceforge.net/project/limitcpu/limitcpu/%{name}-%{version}.tar.gz
# Source0-md5:	bdfae460475241d6253a74abf4dffbad
URL:		https://limitcpu.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpulimit is a simple program that attempts to limit the cpu usage of a
process (expressed in percentage, not in CPU time). This is useful to
control batch jobs, when you don't want they eat too much cpu. It does
not act on the nice value or other scheduling priority stuff, but on
the real cpu usage. Also, it is able to adapt itself to the overall
system load, dynamically and quickly.

%description -l pl.UTF-8
cpulimit to prosty program ograniczający zużycie procesora przez
proces (wyrażone w procentach, nie w czasie CPU). Jest to przydatne to
kontrolowania zadań wsadowych, żeby nie wykorzystywały zbyt dużo mocy
procesora. Program ten nie operuje na wartości nice czy innych
priorytetach kolejkowania, ale na rzeczywistym czasie działania.
Program jest też w stanie dynamicznie dostosować się do obciążenia
systemu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/cpulimit
%{_mandir}/man1/cpulimit.1*
