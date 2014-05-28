# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kf5-kplotting
Summary:    KDE Frameworks 5 Tier 1 addon for plotting
Version:    4.99.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kplotting.yaml
Source101:  kf5-kplotting-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  perl
BuildRequires:  pcre-devel


%description
KPlotting provides classes to do plotting.



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.



%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
# << install post









%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/KPlotting
%{_kf5_includedir}/kplotting_version.h
%{_kf5_libdir}/libKF5Plotting.so
%{_kf5_libdir}/cmake/KF5Plotting
%{_datadir}/qt5/mkspecs/modules/qt_KPlotting.pri
# >> files devel
# << files devel

