%global octpkg tsa

Summary:	Time series analysis methods for Octave
Name:		octave-tsa
Version:	4.6.3
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/tsa/
Source0:	https://downloads.sourceforge.net/octave/tsa-%{version}.tar.gz

BuildRequires:  octave-devel >= 2.9.7
BuildRequires:  octave-nan >= 3.0.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-nan >= 3.0.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Stochastic concepts and maximum entropy methods for time series 
analysis in Octvave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

