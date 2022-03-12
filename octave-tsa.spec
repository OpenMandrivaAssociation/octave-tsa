%global octpkg tsa

Summary:	Time series analysis methods for Octave
Name:		octave-%{octpkg}
Version:	4.6.3
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.7
BuildRequires:	octave-nan > 3.0.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-nan > 3.0.0

Requires(post): octave
Requires(postun): octave

%description
Stochastic concepts and maximum entropy methods for time series analysis
in Octvave.

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
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

