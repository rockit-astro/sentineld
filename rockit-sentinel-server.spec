Name:      rockit-sentinel-server
Version:   %{_version}
Release:   1
Url:       https://github.com/rockit-astro/sentineld
Summary:   Sentinel feed client for the NGTS telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-requests python3-xml2dict python3-rockit-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/sentineld %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/sentineld.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/sentineld
%defattr(-,root,root,-)
%{_unitdir}/sentineld.service

%changelog
