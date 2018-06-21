#%define version __DECISIONENGINE_RPM_VERSION__
#%define release __DECISIONENGINE_RPM_RELEASE__
%define version 0.3.1
%define release 0.2

%define de_user decisionengine
%define de_group decisionengine

%define de_confdir %{_sysconfdir}/decisionengine
%define de_channel_confdir %{_sysconfdir}/decisionengine/config.d
%define de_logdir %{_localstatedir}/log/decisionengine
%define de_lockdir %{_localstatedir}/lock/decisionengine
%define systemddir %{_prefix}/lib/systemd/system

# From http://fedoraproject.org/wiki/Packaging:Python
# Define python_sitelib
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define de_python_sitelib $RPM_BUILD_ROOT%{python_sitelib}

Name:           decisionengine
Version:        %{version}
Release:        %{release}
Summary:        The HEPCloud Decision Engine Framework

Group:          System Environment/Daemons
License:        Fermitools Software Legal Information (Modified BSD License)
URL:            http://hepcloud.fnal.gov

Source0:        decisionengine.tar.gz

BuildArch:      x86_64
BuildRequires:  cmake numpy numpy-f2py python-pandas
BuildRequires:  boost-python boost-regex boost-system
Requires:       numpy >= 1.7.1
Requires:       numpy-f2py >= 1.7.1
Requires:       python-pandas >= 0.17.1
Requires:       boost-python >= 1.53.0
Requires:       boost-regex >= 1.53.0
Requires:       boost-system >= 1.53.0
Requires(post): /sbin/service
Requires(post): /usr/sbin/useradd


%description
The Decision Engine is a critical component of the HEPCloud Facility. It
provides the functionality of resource scheduling for disparate resource
providers, including those which may have a cost or a restricted allocation
of cycles.

%package testcase
Summary:        The HEPCloud Decision Engine Test Case
Group:          System Environment/Daemons
Requires:       decisionengine

%description testcase
The testcase used to try out the Decision Engine.


%package standard-library
Summary:        The HEPCloud Decision Engine Modules in Standard Library
Group:          System Environment/Daemons
Requires:       decisionengine

%description standard-library
The modules in the Decision Engine Standard Library.


%prep
%setup -q -n decisionengine


%build


%install
rm -rf $RPM_BUILD_ROOT

# Create the system directories
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_initddir}
install -d $RPM_BUILD_ROOT%{de_confdir}
install -d $RPM_BUILD_ROOT%{de_channel_confdir}
install -d $RPM_BUILD_ROOT%{de_logdir}
install -d $RPM_BUILD_ROOT%{de_lockdir}
install -d $RPM_BUILD_ROOT%{systemddir}
install -d $RPM_BUILD_ROOT%{python_sitelib}

# Copy files in place
cp -r ../decisionengine $RPM_BUILD_ROOT%{python_sitelib}

mkdir -p $RPM_BUILD_ROOT%{de_confdir}/config.d
# BUILDING testcase RPM: Uncomment following 1 line
#install -m 0644 framework/tests/etc/decisionengine/config.d/channelA.conf $RPM_BUILD_ROOT%{de_channel_confdir}

# Remove unwanted files
rm -Rf $RPM_BUILD_ROOT%{python_sitelib}/decisionengine/build
# BUILDING testcase RPM: Comment following line
rm -Rf $RPM_BUILD_ROOT%{python_sitelib}/decisionengine/testcases

# BUILDING testcase RPM: Uncomment following 3 lines
#%files testcase
#%{python_sitelib}/decisionengine/testcases
#%config(noreplace) %{de_channel_confdir}/channelA.conf


%files standard-library
%{python_sitelib}/decisionengine/__init__.py
%{python_sitelib}/decisionengine/__init__.pyo
%{python_sitelib}/decisionengine/__init__.pyc
%{python_sitelib}/decisionengine/LICENSE.txt
%{python_sitelib}/decisionengine/modules


%pre


%post

%preun

%changelog
* Tue Dec 12 2017 Parag Mhashilkar <parag@fnal.gov> - 0.3.1-0.1
- Minor bug fixes

* Mon Nov 13 2017 Parag Mhashilkar <parag@fnal.gov> - 0.3-0.1
- Decision Engine v0.3
- Includes fixes made during the demo

* Thu Nov 02 2017 Parag Mhashilkar <parag@fnal.gov> - 0.2-0.1
- Decision Engine v0.2 for the demo
- RPM work in progress

* Fri Sep 15 2017 Parag Mhashilkar <parag@fnal.gov> - 0.1-0.2
- Decision Engine v0.1 work in progress
- Added packaging for modules

* Mon May 01 2017 Parag Mhashilkar <parag@fnal.gov> - 0.1-0.1
- Decision Engine v0.1
- RPM work in progress

