Summary: Reverse Proxy Add Forward module for Apache
Name: mod_rpaf
Version: 0.6
Release: 1%{?dist}
License: Apache
Group: System Environment/Daemons
URL: https://github.com/sakuro/mod_rpaf-0.6
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: httpd-devel
Requires: httpd

%description
rpaf is for backend Apache servers what mod_proxy_add_forward is for
frontend Apache servers. It does excactly the opposite of
mod_proxy_add_forward written by Ask Bjørn Hansen. It will also work
with mod_proxy in Apache starting with release 1.3.25 and mod_proxy
that is distributed with Apache2 from version 2.0.36.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -m0755 -d $RPM_BUILD_ROOT$(/usr/bin/apxs -q LIBEXECDIR)%{_libdir}/httpd/modules
make DESTDIR=$RPM_BUILD_ROOT install
install -m0644 -D mod_rpaf.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/mod_rpaf.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/mod_rpaf-2.0.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_rpaf.conf

%changelog
* Thu Apr 26 2016 OZAWA Sakuro <ozawa@feedforce.jp>
- Initial package
