## SCOPE

-- Can make draft,submit and delete travel forms.
-- Approvals and rejection for MANAGER and FINANCIAL MANAGER
-- Login mechanism and logic is based of django's built in login tool.
-- Computation is dynamic.
-- Roles are based on Django grouping table

## LIMITATIONS

-- No design
-- Did not put local coveyance, due to lack of understanding in this department of logic
-- Did not put Request for Information, I believe that should be grounds for rejection already and refiling so it is logged
-- Computation is dynamic which is why I made the computation part of the travel details in text form to 
   log its computation even though this is not normalized.
-- No indexing, for testing purposes only.
-- No maps and images, due to the API's I've found has credit card payment

## Requirements
exam/etx/pip_requirements.txt

#Fixins
exam/fixtures/*_main.json
