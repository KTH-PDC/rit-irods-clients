Name:		rit-irods-clients
Version:	1.0.0
Release:	1
Summary:	Client-applications and libraries for iRODS.

Group:		Applications
License:	BSD
URL:		https://github.com/MaastrichtUniversity/rit-irods-clients
Source0:	https://github.com/MaastrichtUniversity/rit-irods-clients/archive/1.0.0.tar.gz

Requires:	irods-runtime >= 4.1.8

%description
iRODS iping utility from https://github.com/irods/contrib as packaged by University of Maastricht and KTH Royal Institute of Technology.

%prep
%setup -q -c 


%build
(cd %{name}-%{version}/iping/src; make install)

%install
mkdir -p %{buildroot}/usr/bin
cp %{name}-%{version}/iping/build/iping %{buildroot}/usr/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) /usr/bin/iping

%changelog
* Wed Apr 05 2017 Ilari Korhonen <ilarik@kth.se>
* initial rpm release version 1.0.0
