//
//  MTText.swift
//
        
import UIKit
        
enum MTText: String {
        
   case txt_hello
   case txt_down_the_line
   case txt_the_sum
   case txt_tap_to_continue
   case txt_terms_and_conditions

}

extension MTText {
    var text: String {
        return rawValue
    }

    var localized: String {
        let language = Locale.preferredLanguages.first ?? "en"
        if let path = Bundle.main.path(forResource: language, ofType: "lproj") {
            let bundle = Bundle(path: path)
            if let string = bundle?.localizedString(forKey: text, value: nil, table: nil) {
                return string.capFirstLetter()
            }
        }
        
        return NSLocalizedString(text, comment: "").capFirstLetter()
    }
    
    func format(_ arguments: CVarArg...) -> String {
        let value = NSLocalizedString(text, comment: "")
        return String(format: value, arguments: arguments)
    }
    
    static func updateLocalize(_ lang: String) {
        UserDefaults.standard.setValue([lang], forKey: "AppleLanguages")
    }
}

extension String {
    func capFirstLetter() -> String {
        return self.isEmpty ? self : prefix(1).capitalized + dropFirst()
    }

    mutating func capitalizeFirstLetter() {
        self = self.capitalizingFirstLetter()
    }
}