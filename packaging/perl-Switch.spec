#
# spec file for package perl-Switch
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           perl-Switch
Version:        2.16
Release:        4
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Switch
Summary:        A switch statement for Perl
Url:            http://search.cpan.org/dist/Switch/
Group:          Development/Libraries
Source:         http://www.cpan.org/authors/id/R/RG/RGARCIA/%{cpan_name}-%{version}.tar.gz
Source1001: 	perl-Switch.manifest
BuildRequires:  perl
BuildRequires:  perl-macros
BuildArch:      noarch

%description
The Switch.pm module implements a generalized case mechanism that covers
most (but not all) of the numerous possible combinations of switch and case
values described above.

The module augments the standard Perl syntax with two new control
statements: 'switch' and 'case'. The 'switch' statement takes a single
scalar argument of any type, specified in parentheses. 'switch' stores this
value as the current switch value in a (localized) control variable. The
value is followed by a block which may contain one or more Perl statements
(including the 'case' statement described below). The block is
unconditionally executed once the switch value has been cached.

%prep
%setup -q -n %{cpan_name}-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%manifest %{name}.manifest
%defattr(-,root,root,755)

%changelog
