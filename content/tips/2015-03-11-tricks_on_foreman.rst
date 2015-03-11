Title: Tricks on Foreman
Tags: foreman, yaml
Author: Claudinei Matos
Status: Draft

Dynamic variables
<%=@host.name%>

reference: http://www.theforeman.org/manuals/1.6/index.html#4.2.4SmartVariables
http://projects.theforeman.org/projects/foreman/wiki/templatewriting


Para pegar o ip de uma interface especifica:

* Habiitar safemode_render em Settings / Provisioning
* Adicionar no parameter: <%=@host.facts_hash['ipaddress_ethX']%>
