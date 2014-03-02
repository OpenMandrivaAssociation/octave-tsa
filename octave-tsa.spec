%define	pkgname tsa

Summary:	Time series analysis methods for Octave
Name:       octave-%{pkgname}
Version:	4.1.1
Release:       3
Source0:	%{pkgname}-%{version}.tgz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/tsa/
Conflicts:	octave-forge <= 20090607
Requires:	octave, octave-nan >= 1.0.0
BuildRequires:  octave-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch

%description
Stochastic concepts and maximum entropy methods for time series
analysis in Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tgz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .
mv %{pkgname}/doc/README.TXT .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%doc COPYING DESCRIPTION README.TXT
%{_datadir}/octave/packages/%{pkgname}-%{version}
