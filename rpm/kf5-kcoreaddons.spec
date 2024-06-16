%global kf5_version 5.116.0
%global framework kcoreaddons

Name: opt-kf5-kcoreaddons
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kcoreaddons

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires:  make
BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel
BuildRequires:  shared-mime-info
BuildRequires:  systemd-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kcoreaddons5_qt
%find_lang_kf5 kde5_xml_mimetypes
cat *.lang > all.lang


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kcoreaddons.*
%{_opt_kf5_bindir}/desktoptojson
%{_opt_kf5_libdir}/libKF5CoreAddons.so.*
%{_opt_kf5_datadir}/mime/packages/kde5.xml
%{_opt_kf5_datadir}/kf5/licenses/
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KCoreAddons/
%{_opt_kf5_libdir}/libKF5CoreAddons.so
%{_opt_kf5_libdir}/cmake/KF5CoreAddons/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KCoreAddons.pri

