Summary:	CPU usage limiter
Summary(pl):	Ograniczanie wykorzystania procesora
Name:		cpulimit
Version:	1.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cpulimit/%{name}-%{version}.tar.gz
# Source0-md5:	8f8d795f5c6a6b5483da4c200a8df9ee
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
cpulimit to prosty program ograniczaj±cy zu¿ycie procesora przez
proces (wyra¿one w procentach, nie w czasie). Jest to przydatne to
kontrolowania zadañ wsadowych, kiedy nie chcesz, by wykorzystywa³y
zbyt du¿o mocy procesora. Program ten nie operuje na warto¶ci nice czy
priorytetach kolejkowania, ale na rzecywistym czasie dzia³ania.
Program jest te¿ w stanie dynamicznie dostosowaæ siê do obci±¿enia
systemu.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} -lrt cpulimit.c -o cpulimit

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
