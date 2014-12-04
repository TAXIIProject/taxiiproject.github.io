---
layout: flat_for_idioms
title: TAXII Service Profiles
---

<link href="/css/idioms.css" rel="stylesheet"/>
Sometimes TAXII implementers know which capabilities they'd like to implement, but don't really know where to start.
TAXII Service Profiles are meant to help with that.

TAXII Service Profiles document design patterns and requirements for common TAXII use cases, providing implementers 
with concrete information on how TAXII can be used to exchange threat information. TAXII Service Profiles include 
Use Case description, requirements, and example technical materials where possible. TAXII Service Profiles primarily 
focus on the TAXII Server, as it is usually the more complex component, though TAXII Clients are described as well.

When possible, implementers whose use cases match a use cases defined by a TAXII Service Profile are recommended to 
implement the TAXII Service Profile(s) that match their use case.
 
While conforming to TAXII Service Profiles is optional (a TAXII implementation can conform to as many or as few 
as desired), any implementation claiming conformance with a particular TAXII Service Profile MUST adhere to all 
requirements in the TAXII Service Profile they are claiming conformance with.

The list can be filtered based on use case categories, as well as by which TAXII Services they use.

<h3><font color="red">TAXII Service Profiles are still being worked on, and there will be an announcement as they go live!</font></h3> 

<div class="row">
  <div class="col-md-12">
    {% assign use_case_list = "Reputation" %}
    {% assign service_list = "Discovery Service,Poll Service,Inbox Service,Collection Management Service" %}
    <table id="idiom-table" class="table table-striped">
      <thead>
        <tr>
          <th>
            <h3>Service Profile
              <small class="dropdown">
                <button class="btn btn-info dropdown-toggle" type="button" id="filterMenu" data-toggle="dropdown">
                  Filter By... <span class="caret"></span>
                </button>
                <ul id="tag-filterer" class="dropdown-menu" role="menu" aria-labelledby="filterMenu">
                  <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">None</a></li>
                  <li role="presentation" class="divider"></li>
                  <li role="presentation" class="dropdown-header">Use Cases</li>
                  {% assign use_cases = use_case_list | split:"," | sort %}
                  {% for use_case in use_cases %}
                    <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{use_case}}</a></li>
                  {% endfor %}
                  <li role="presentation" class="divider"></li>
                  <li role="presentation" class="dropdown-header">TAXII Services</li>
                  {% assign services = service_list | split:"," | sort %}
                  {% for service in services %}
                    <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{service}}</a></li>
                  {% endfor %}
                </ul>
              </small>
            </h3>
          </th>
          <th>
            <h3>Use Cases</h3>
          </th>
          <th>
            <h3>TAXII Services</h3>
          </th>
          <th>
            <h3>Description</h3>
          </th>
        </tr>
      </thead>
      <tbody>
      
      {% comment %} UNCOMMENT THIS WHEN SERVICE PROFILES ARE READY
      
        {% for page in site.pages %}
          {% if page.use_cases | size != 0  or page.services | size != 0 %}
            <tr>
              <td>
                <h4>
                  <a href='{{page.url | remove: "/index.html"}}'>{{page.title}}</a>
                </h4>
              </td>
              <td>
                <span class="tag-labels-container">
                  {% for use_case in page.use_cases %}
                    {% assign tag = use_case | replace:' ','-' | downcase %}
                    <span data-tag="{{use_case}}" class="label label-{{tag}}">
                      {{use_case}}
                    </span>
                  {% endfor %}
                </span>
              </td>
              <td>
                {% for service in page.services %}
                {% assign tag = service | replace:' ','-' | downcase %}
                <span class="idiom-construct" data-tag="{{service}}" data-toggle="tooltip"
                    data-placement="top" title="{{service}}">
                  <img src="/images/{{service}}.png" width="40px" alt="{{service}} Icon" />
                </span>
                {% endfor %}
              </td>
              <td>
                <button class="btn btn-info" data-toggle="popover" data-placement="left" data-trigger="hover" title="{{page.title}}" data-content="{{page.summary | escape}}">
                  <span class="glyphicon glyphicon-question-sign"><span>
                </button>
              </td>
            </tr>
          {% endif %}
        {% endfor %}
        
        {% endcomment %}
      </tbody>
    </table>
  </div>
</div>