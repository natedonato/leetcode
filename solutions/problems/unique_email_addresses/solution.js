/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const count = {};

    emails.forEach (email => {
        let [localName, domainName] = email.split("@");        
        localName = localName.split("+")[0].split("").filter(el => el != ".").join('');
        console.log(localName, domainName)
        count[`${localName}*${domainName}`] = true;
    })
    return Object.keys(count).length;
    
};