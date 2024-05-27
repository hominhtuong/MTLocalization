//
//  ViewController.swift
//  Example
//
//  Created by Hồ Minh Tường on 29/01/2024.
//

import MiTu
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        
        let helloLabel = UILabel()
        helloLabel >>> view >>> {
            $0.snp.makeConstraints {
                $0.center.equalToSuperview()
            }
            $0.backgroundColor = .random.withAlphaComponent(0.39)
            $0.textColor = .black
            $0.numberOfLines = 0
            $0.text = MTText.txt_hello.localized
            
        }
        
        let downLineLabel = UILabel()
        downLineLabel >>> view >>> {
            $0.snp.makeConstraints {
                $0.top.equalTo(helloLabel.snp.bottom).offset(16)
                $0.centerX.equalToSuperview()
            }
            $0.backgroundColor = .random.withAlphaComponent(0.39)
            $0.textColor = .black
            $0.numberOfLines = 0
            $0.text = MTText.txt_down_the_line.localized
        }
        
        let theSumLabel = UILabel()
        theSumLabel >>> view >>> {
            $0.snp.makeConstraints {
                $0.top.equalTo(downLineLabel.snp.bottom).offset(16)
                $0.centerX.equalToSuperview()
            }
            $0.backgroundColor = .random.withAlphaComponent(0.39)
            $0.textColor = .black
            $0.numberOfLines = 0
            $0.text = MTText.txt_the_sum.format("4", "5", "\(4 + 5)")
        }
        
        let tapToContinueLabel = UILabel()
        tapToContinueLabel >>> view >>> {
            $0.snp.makeConstraints {
                $0.top.equalTo(theSumLabel.snp.bottom).offset(16)
                $0.centerX.equalToSuperview()
            }
            $0.backgroundColor = .random.withAlphaComponent(0.39)
            $0.textColor = .black
            $0.numberOfLines = 0
            $0.text = MTText.txt_tap_to_continue.localized
        }
        
        let termsAndConditionsLabel = UILabel()
        termsAndConditionsLabel >>> view >>> {
            $0.snp.makeConstraints {
                $0.top.equalTo(tapToContinueLabel.snp.bottom).offset(16)
                $0.centerX.equalToSuperview()
            }
            $0.backgroundColor = .random.withAlphaComponent(0.39)
            $0.textColor = .black
            $0.numberOfLines = 0
            $0.text = MTText.txt_terms_and_conditions.localized
        }
    }


}

