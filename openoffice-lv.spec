Name: openoffice-lv
Summary: Latvian linguistic dictionaries
Version: 0.8.2
Release: 2%{?dist}
Source: http://dict.dv.lv/dl/dict_lv_LV-%{version}.oxt
Group: Applications/Text
URL: http://dict.dv.lv/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

%description
Latvian linguistic dictionaries.

%package -n hunspell-lv
Summary: Latvian hunspell dictionaries
Group: Applications/Text
Requires: hunspell

%description -n hunspell-lv
Latvian hunspell dictionaries.

%package -n hyphen-lv
Summary: Latvian hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-lv
Latvian hyphenation rules.

%package -n mythes-lv
Summary: Latvian thesaurus
Group: Applications/Text

%description -n mythes-lv
Latvian thesaurus.

%prep
%setup -q -c

%build
for i in README_lv_LV.txt README_hyph_lv_LV.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-4 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p lv_LV.dic lv_LV.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hyph_lv_LV.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p th_lv_LV_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files -n hunspell-lv
%defattr(-,root,root,-)
%doc README_lv_LV.txt
%{_datadir}/myspell/*

%files -n hyphen-lv
%defattr(-,root,root,-)
%doc README_hyph_lv_LV.txt
%{_datadir}/hyphen/*

%files -n mythes-lv
%defattr(-,root,root,-)
%doc package-description.txt
%{_datadir}/mythes/*

%changelog
* Fri Jun 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.8.2-2
- Resolves: rhbz#602691 clarify licence

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.8.2-1.1
- Rebuilt for RHEL 6

* Sat Sep 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.8.2-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.8-0.2.b1
- tidy spec

* Mon May 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.8-0.1.b1
- latest version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.7.4-1
- latest version

* Sat Sep 20 2008 Caolan McNamara <caolanm@redhat.com> - 0.7.3-1
- initial version
