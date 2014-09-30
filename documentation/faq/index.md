---
layout: flat
title: TAXII FAQ
---

TAXII FAQ are questions and answers to questions that have been asked about the TAXII Specifications.

New questions, comments, or clarifications can be posted to the TAXII Discussion List or sent to taxii@mitre.org.

## TAXII (General)

### T-Q1: in_response_to is unknown

**Q:** In certain cases, a TAXII Server is expected to respond to a TAXII Client with a Status Message but the
message_id of the request message cannot be known. For example, consider an unparseable request message; that message
should be met with a Status Message with a Status Type of BAD_MESSAGE. However, in_response_to is required but
cannot be retrieved from the request message because it could not be parsed. What should be used for the in_response_to
field of that Status Message?

**A:** The short answer is, use '0' as the in_response_to field. The long answer is that this is a corner case that
wasn't fully realized until after TAXII 1.1 was released, and therefore there isn't a "standard" way to respond. The
TAXII Team proposes using '0' as a convention for cases where the message_id of the request is not known.

## TAXII Default Query 1.0

### TDQ-Q1: match_type vs. case_sensitive_string

**Q:** In Sections 5.1.1 and 5.1.2 there is the parameter match_type with the permitted values case_sensitive_string 
and case_insentive_string, yet in Sections 5.1.9, 5.1.10, 5.1.11 and 5.2.1 there is the parameter case_sensitive 
with the permitted values of TRUE and FALSE.

**A:**
The reasoning behind these differences is that the relationships defined in Sections 5.1.1 (equals) and 5.1.2 
(not equals) can be a string operation or a numeric operation, while the others are string operations only. In the 
case of a numeric equals, a ‘case_insensitive_string’ parameter doesn’t make sense. In the case of Sections 5.1.9 
(begins_with), 5.1.10 (ends_with), 5.1.11 (contains), and 5.2.1 (regex matches), they are all string match operations.
For the string matching operations, we went with a “case_sensitive=True/False” property and for operations that are 
not necessarily string matching we have a “match_type” property.

### TDQ-Q2: greater_than_or_equal vs. greater_than_or_equals

**Q:** In Sections 5.1.4 and 5.1.6 there are the relationships greater_than_or_equal and less_then_or_equal, 
yet in Sections 5.3.3 and 5.3.5 the relationships are listed as greater_then_or_equals and less_then_or_equals.

**A:** Good catch. This was an oversight on our part and consistency was intended. Hopefully this does not make 
implementation of the specification any more difficult.

### TDQ-Q3: does_not_exist and exists

**Q;** In Sections 5.1.7 and 5.1.8. the relationships does_not_exist and exists do not have any parameters. 
Should there be a parameter to indicate what does not exists and what exists?

**A:** The intent of the relationships (exists, does_not_exist, among others) are intended to be used in a Criterion 
structure as described in section 3.1.1. In a Criterion there is a Target and Test. In the case of exists and 
does_not_exist, the target is tested for (non) existence.

### TDQ-Q4: Definition for does_not_exists is incorrect

**Q:** In Section 5.1.7 the text description is inconsistent with the relationship type. "The greater 
then relationship returns true if the target does not exists"  Should this read "The does not 
exist relationship returns true if the target does not exist."

**A:** You are correct, this is a typo. We’ll have to update the errata.

### TDQ-Q5: Criterion/@negate

**Q:** The @negate property of Criterion reads 'This field indicates whether the final result of the Criterion should 
be negated. If absent, treat this field as "false".' What is the correct interpretation of this statement?
  
**A:** The Criterion negates the result of the evaluating a Criterion. Each Criterion has a Test and Target. 
The Test is applied to the Target, resulting in a True (The Target matches the test) or a False (The Target does 
not match the Test). If the negate property is set to "true", the result is "negated": True becomes False and 
False becomes True.

As a simple example, let's say you have a simple record that has a single property, "height=100". If you have
 Target=height and a Test of "equals 100", the Criterion would evaluate to true for the "height=100" record. 
 If negate is set to true, the Criterion would instead evaluate to false.
